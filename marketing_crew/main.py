from datetime import datetime
import os
import time
from crew import TheMarketingCrew

# Create output directory
os.makedirs("output", exist_ok=True)

# Simple inputs
inputs = {
    "product_name": "Multi-Agent AI Research",
    "target_audience": "Developers and Researchers",
    "product_description": "Advanced multi-agent artificial intelligence systems",
    "budget": "Research Project",
    "current_date": datetime.now().strftime("%Y-%m-%d")
}

print("Starting Complete Marketing Crew...")
print("Output will be saved in /output/ folder")

crew = TheMarketingCrew()

# Run with retry logic
max_retries = 3
for attempt in range(max_retries):
    try:
        print(f" Attempt {attempt + 1} of {max_retries}")
        result = crew.marketing_crew().kickoff(inputs=inputs)

        # Save final result
        with open("output/final_result.md", "w", encoding="utf-8") as f:
            f.write("# Marketing Crew Final Output\n")
            f.write("Generated on: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n\n")
            f.write(str(result))

        print(" SUCCESS! All tasks completed!")
        print(" Check /output/ folder for generated files:")
        print("   - market_research.md")
        print("   - content_strategy.md")
        print("   - blog_post.md")
        print("   - social_media_post.md")
        print("   - seo_optimized_blog.md")
        print("   - final_result.md")
        break

    except Exception as e:
        error_msg = str(e)
        print(f" Error: {error_msg}")

        if "rate_limit" in error_msg.lower() or "429" in error_msg:
            wait_time = 10 * (attempt + 1)
            print(f"⏳ Waiting {wait_time} seconds...")
            time.sleep(wait_time)
        else:
            print(" Non-rate-limit error. Stopping.")
            break
else:
    print(" All attempts failed. Please try again later.")