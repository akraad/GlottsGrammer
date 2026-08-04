import os
import json

base_dir = os.path.expanduser("~/Desktop/GlottsGrammer/content/grammar/en")
locales = ["fa", "ar", "de", "es", "fr", "hi", "ja", "pt", "ru", "tr"]

def load_json(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return None

total_topics = 0
missing_files = []
incomplete_files = []

print("======================================================================")
print("🔍 CHECKING ENGLISH GRAMMAR TRANSLATIONS COVERAGE (10 LOCALES)")
print("======================================================================")

for root, dirs, files in os.walk(base_dir):
    if "base.json" in files and "i18n" in dirs:
        total_topics += 1
        rel_path = os.path.relpath(root, base_dir)
        i18n_dir = os.path.join(root, "i18n")
        
        for loc in locales:
            i18n_path = os.path.join(i18n_dir, f"{loc}.json")
            
            # 1. Check file existence
            if not os.path.exists(i18n_path):
                missing_files.append((rel_path, loc))
                continue
            
            # 2. Check content completeness
            data = load_json(i18n_path)
            if not data:
                incomplete_files.append((rel_path, loc, "Invalid JSON structure"))
                continue
                
            missing_fields = []
            for field in ["title", "summary", "explanation"]:
                if not data.get(field) or str(data.get(field)).strip() == "":
                    missing_fields.append(field)
            
            if missing_fields:
                incomplete_files.append((rel_path, loc, f"Missing fields: {', '.join(missing_fields)}"))

# Report Summary
print(f"📊 Total English Topics Scanned: {total_topics}")
print(f"🌐 Target Locales Checked Per Topic: {len(locales)}")
print(f"📂 Total Translation Files Checked: {total_topics * len(locales)}")
print("----------------------------------------------------------------------")

if not missing_files and not incomplete_files:
    print("🎉 PERFECT! All English grammar topics have 100% COMPLETE translations for all 10 locales!")
else:
    if missing_files:
        print(f"\n❌ MISSING TRANSLATION FILES ({len(missing_files)}):")
        for topic, loc in missing_files:
            print(f"   ├─ Topic: {topic}")
            print(f"   └─ Missing Locale: {loc}.json")
            
    if incomplete_files:
        print(f"\n⚠️ INCOMPLETE TRANSLATIONS ({len(incomplete_files)}):")
        for topic, loc, reason in incomplete_files:
            print(f"   ├─ Topic: {topic} [{loc}.json]")
            print(f"   └─ Issue: {reason}")

print("======================================================================")
