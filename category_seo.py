import os
import re

# Meta descriptions for each category
category_descriptions = {
    "biomarkers.html": "Discover key health biomarkers and how to optimize them. Learn about metrics that matter for longevity and performance.",
    "body.html": "Explore fitness, health and body optimization strategies. Workouts, recovery techniques and physical wellbeing.",
    "finance.html": "Smart personal finance tips, wealth building strategies and money management for a balanced life.",
    "fitness.html": "Fitness workouts, training tips and exercise guides for all levels. Build strength and endurance.",
    "habits-growth.html": "Build powerful habits and accelerate personal growth. Science-backed strategies for self-improvement.",
    "home-wellness.html": "Create a healthy home environment. Tips for wellness-focused living spaces and home habits.",
    "hot.html": "Explore emerging trends and cutting-edge topics in health, wellness and lifestyle technology.",
    "lifestyle.html": "Modern lifestyle tips for balance and fulfillment. Navigate work, life and personal wellbeing.",
    "living.html": "Guides for intentional living. Daily practices for a more meaningful and balanced lifestyle.",
    "longevity.html": "Longevity science and anti-aging strategies. Evidence-based approaches to extend healthspan.",
    "mental-fitness.html": "Train your mind with mental fitness exercises. Cognitive hacks for better thinking and focus.",
    "mind.html": "Mindfulness, meditation and mental health resources. Train your mind for peace and clarity.",
    "nutrition.html": "Evidence-based nutrition advice and diet strategies. Fuel your body for optimal performance.",
    "reviews.html": "Honest product reviews for health, fitness and wellness. Make informed purchasing decisions.",
    "routine.html": "Build powerful daily routines. Optimize your mornings, evenings and daily habits.",
    "sleep.html": "Improve sleep quality with science-backed tips. Master recovery and rest for better health.",
    "sports.html": "Sports performance training and athletic tips. Elevate your game with expert guidance.",
    "supplements.html": "Evidence-based supplement reviews and guides. Find the best supplements for your goals.",
    "tech-lifestyle.html": "Where technology meets lifestyle. Digital tools and gadgets for modern living.",
    "wearables.html": "Fitness tracker reviews and wearable tech guides. Optimize yourQuantified Self journey.",
    "wellness.html": "Comprehensive wellness resources for mind, body and spirit. Your complete health guide.",
    "yoga.html": "Yoga poses, practices and philosophy. Find balance through ancient movement practices."
}

for filename, description in category_descriptions.items():
    filepath = f"category/{filename}"
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            content = f.read()
        
        # Check if meta description already exists
        if '<meta name="description"' not in content:
            # Add after <title>
            title_match = re.search(r'(<title>.*?</title>)', content, re.DOTALL)
            if title_match:
                meta_desc = f'\n    <meta name="description" content="{description}">'
                content = content.replace(title_match.group(1), title_match.group(1) + meta_desc)
                
                with open(filepath, 'w') as f:
                    f.write(content)
                print(f"✓ Updated {filepath}")
        else:
            print(f"⏭ Already has meta desc: {filepath}")

print("Done with category pages!")
