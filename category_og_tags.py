import os
import re

# Category descriptions for OG tags
category_descriptions = {
    "biomarkers.html": "Discover key health biomarkers and how to optimize them.",
    "body.html": "Explore fitness, health and body optimization strategies.",
    "finance.html": "Smart personal finance tips and wealth building strategies.",
    "fitness.html": "Fitness workouts, training tips and exercise guides.",
    "habits-growth.html": "Build powerful habits and accelerate personal growth.",
    "home-wellness.html": "Create a healthy home environment.",
    "hot.html": "Explore emerging trends in health and wellness.",
    "lifestyle.html": "Modern lifestyle tips for balance and fulfillment.",
    "living.html": "Guides for intentional and meaningful living.",
    "longevity.html": "Longevity science and anti-aging strategies.",
    "mental-fitness.html": "Mental fitness exercises and cognitive hacks.",
    "mind.html": "Mindfulness, meditation and mental health resources.",
    "nutrition.html": "Evidence-based nutrition advice and diet strategies.",
    "reviews.html": "Honest product reviews for health and wellness.",
    "routine.html": "Build powerful daily routines.",
    "sleep.html": "Improve sleep quality with science-backed tips.",
    "sports.html": "Sports performance training and athletic tips.",
    "supplements.html": "Evidence-based supplement reviews and guides.",
    "tech-lifestyle.html": "Where technology meets lifestyle.",
    "wearables.html": "Fitness tracker reviews and wearable tech.",
    "wellness.html": "Comprehensive wellness resources.",
    "yoga.html": "Yoga poses, practices and philosophy."
}

for filename, description in category_descriptions.items():
    filepath = f"category/{filename}"
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            content = f.read()
        
        # Check if OG tags already exist
        if '<meta property="og:' not in content:
            # Extract title
            title_match = re.search(r'<title>(.*?) \|', content)
            if title_match:
                title = title_match.group(1)
            else:
                title = "Boldly Balanced"
            
            og_tags = f'''
    <!-- Open Graph -->
    <meta property="og:title" content="{title} | Boldly Balanced">
    <meta property="og:description" content="{description}">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://vitalwell.vercel.app/category/{filename}">
    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{title} | Boldly Balanced">
    <meta name="twitter:description" content="{description}">'''
            
            # Add after description meta tag
            if '<meta name="description"' in content:
                content = re.sub(
                    r'(<meta name="description" content="[^"]*">)',
                    r'\1' + og_tags,
                    content
                )
                
                with open(filepath, 'w') as f:
                    f.write(content)
                print(f"✓ OG/Twitter tags added: {filepath}")
        else:
            print(f"⏭ Already has OG tags: {filepath}")

print("Done with category OG tags!")
