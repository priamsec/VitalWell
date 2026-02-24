#!/bin/bash
# Add Article schema to all blog posts

POSTS_DIR="/home/frn/.openclaw/shared/VitalWell/posts"
GUIDES_DIR="/home/frn/.openclaw/shared/VitalWell/guides"

# Function to add schema to a file
add_schema() {
    local file="$1"
    local dir="$2"
    
    # Get filename without path
    local filename=$(basename "$file")
    
    # Extract title from <title> tag (format: "Title | Boldly Balanced")
    local title=$(grep -oP '(?<=<title>)[^|]+' "$file" | head -1 | sed 's/[[:space:]]*$//')
    
    # Try to get description from meta description, or first paragraph
    local description=$(grep -oP '(?<=<meta name="description" content=")[^"]+' "$file" 2>/dev/null | head -1)
    
    # If no meta description, get from first p tag
    if [ -z "$description" ]; then
        description=$(grep -oP '<p>[^<]+</p>' "$file" | head -1 | sed 's/<[^>]*>//g' | head -c 200)
    fi
    
    # Get image from og:image or first img
    local image=$(grep -oP '(?<=<meta property="og:image" content=")[^"]+' "$file" 2>/dev/null | head -1)
    if [ -z "$image" ]; then
        image=$(grep -oP 'src="https://images[^"]+' "$file" | head -1 | sed 's/src="//')
    fi
    
    # Get date from meta or look for date pattern
    local date=$(grep -oP '\d{4}-\d{2}-\d{2}' "$file" | head -1)
    if [ -z "$date" ]; then
        date="2026-02-22"
    fi
    
    # Check if schema already exists
    if grep -q 'application/ld+json' "$file"; then
        echo "Schema already exists in $filename, skipping"
        return
    fi
    
    # Calculate relative path to root
    local rel_path=""
    if [ "$dir" == "posts" ]; then
        rel_path="../"
    else
        rel_path="../"
    fi
    
    # Create the JSON-LD schema
    local schema=$(cat <<EOF
    <!-- Schema.org Article JSON-LD -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "Article",
      "headline": "$title",
      "description": "$(echo "$description" | head -c 200)",
      "image": "$image",
      "author": {
        "@type": "Organization",
        "name": "Boldly Balanced"
      },
      "publisher": {
        "@type": "Organization",
        "name": "Boldly Balanced",
        "logo": {
          "@type": "ImageObject",
          "url": "https://images.unsplash.com/photo-1559757148-5c350d0d3c56?w=200&q=80"
        }
      },
      "datePublished": "$date",
      "dateModified": "$date",
      "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "https://vitalwell.vercel.app/$dir/$filename"
      }
    }
    </script>
    
EOF
)
    
    # Add schema after <head> tag
    sed -i "/<head>/a\\
$schema" "$file"
    echo "Added schema to $filename"
}

# Process posts
for file in "$POSTS_DIR"/*.html; do
    add_schema "$file" "posts"
done

# Process guides
for file in "$GUIDES_DIR"/*.html; do
    add_schema "$file" "guides"
done

echo "Done adding schema to all pages!"