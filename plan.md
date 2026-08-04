# GlottsGrammer — نقشه‌ی راه پروژه

این سند، برنامه‌ی جامع و مرحله‌به‌مرحله‌ی ساخت سیستم گرامر چندزبانه‌ی اپ Glotts است.
هر مرحله که به‌طور کامل انجام شده باشد با علامت ✅ مشخص می‌شود.
این سند می‌تواند گسترش یابد، اما نباید از مسیر اصلی منحرف شود.

---

## وضعیت کلی پروژه

- **زبان‌های پشتیبانی‌شده (i18n):** ۱۱ زبان (ar, de, en, es, fa, fr, hi, ja, pt, ru, tr)
- **سطوح CEFR:** A1, A2, B1, B2, C1, C2
- **دسته‌های گرامری تعریف‌شده:** ۱۰ دسته
- **مفاهیم مشترک (universal concepts):** ۱۰ مورد در `config/universal-concepts.json`
- **زبان هدف فعلی:** English (`en`)
- **گرامرهای ساخته‌شده:** ۴ مورد
- **لغات ساخته‌شده:** ۳۳ مورد

---

## فاز ۰ — راه‌اندازی و زیرساخت (Setup)

این فاز شامل تعریف ساختار مرجع، schemaها، و ابزارهای اعتبارسنجی است.

- ✅ ساخت پوشه‌ی پروژه `GlottsGrammer`
- ✅ ایجاد `config/locales.json` — تعریف دقیق ۱۱ زبان با direction، script، fallback
- ✅ ایجاد `config/levels.json` — تعریف سطح‌های CEFR از A1 تا C2
- ✅ ایجاد `config/categories.json` — ۱۰ دسته‌ی گرامری مشترک
- ✅ ایجاد `config/universal-concepts.json` — مفاهیم گرامری مشترک بین زبان‌ها
- ✅ ایجاد `schemas/grammar-base.schema.json`
- ✅ ایجاد `schemas/grammar-i18n.schema.json`
- ✅ ایجاد `schemas/vocab-base.schema.json`
- ✅ ایجاد `schemas/vocab-i18n.schema.json`
- ✅ ایجاد `scripts/validate.py` — اعتبارسنجی ساختار، cross-reference، و completeness
- ✅ ایجاد `README.md` — راهنمای کلی پروژه

---

## فاز ۱ — ساخت محتوای پایه‌ی انگلیسی سطح A1

هدف: ساخت گرامرهای بنیادین English A1 همراه با ترجمه‌ی کامل ۱۱ زبانه.

### ۱.۱. گرامرهای ساخته‌شده

- ✅ `en.a1.pronoun.personal-subject` — ضمایر فاعلی (I, you, he, she, it, we, they)
  - base.json + ۱۱ فایل i18n (ar, de, en, es, fa, fr, hi, ja, pt, ru, tr)
- ✅ `en.a1.verb.present-simple` — زمان حال ساده (عادت‌ها، واقعیت‌ها، روتین)
  - base.json + ۱۱ فایل i18n
- ✅ `en.a1.verb.base-form` — شکل پایه‌ی فعل و ۵ فرم آن (base, 3rd sg, present part, past, past part)
  - base.json + ۱۱ فایل i18n
  - مثال‌ها: I drink water / They do not drink tea / Does she like water?
  - خطاهای رایج: "I drinks water" → "I drink water" / "Does she likes" → "Does she like"
- ✅ `en.a1.verb.copula-basic` — فعل to be (am/is/are) در حال
  - base.json + ۱۱ فایل i18n
  - مثال‌ها: I am a student / She is not at home / Are you happy today?
  - خطاهای رایج: "I is a student" → "I am a student" / "He are happy" → "He is happy"

### ۱.۲. لغات ساخته‌شده (مرتبط با گرامرهای بالا)

- ✅ `en.verb.drink`
- ✅ `en.noun.water`
- ✅ `en.phrase.every-day`
- ✅ `en.verb.work`
- ✅ `en.noun.student`
- ✅ `en.noun.friend`
- ✅ `en.noun.book`
- ✅ `en.noun.teacher`
- ✅ `en.noun.tea`
- ✅ `en.verb.like` — دوست داشتن / mögen / 好きである
- ✅ `en.verb.want` — خواستن / wollen / 望む
- ✅ `en.verb.have` — داشتن / haben / 持っている
- ✅ `en.verb.do` — انجام دادن / tun / する
- ✅ `en.verb.go` — رفتن / gehen / 行く
- ✅ `en.verb.eat` — خوردن / essen / 食べる
- ✅ `en.verb.see` — دیدن / sehen / 見る
- ✅ `en.verb.come` — آمدن / kommen / 来る
- ✅ `en.verb.be` — بودن / sein / 〜である
- ✅ `en.adj.happy` — خوشحال / glücklich / 幸せな
- ✅ `en.adj.sad` — غمگین / traurig / 悲しい
- ✅ `en.adj.tired` — خسته / müde / 疲れた
- ✅ `en.adj.hungry` — گرسنه / hungrig / 空腹の
- ✅ `en.noun.home` — خانه / Zuhause / 家
- ✅ `en.noun.school` — مدرسه / Schule / 学校
- ✅ `en.noun.work` — کار (مکان) / Arbeit (Ort) / 仕事（場所）

### ۱.۳. گرامرهای باقی‌مانده‌ی A1 (بر اساس dependency graph)

این گرامرها پیش‌نیاز یا مکمل گرامرهای ساخته‌شده هستند و به ترتیب اولویت لیست شده‌اند:

- ⬜ `en.a1.noun.basic-plural` — جمع بستن ساده (s, es, ies, تغییرات irreg)
- ⬜ `en.a1.noun.definiteness-basic` — a/an/the
- ⬜ `en.a1.pronoun.personal-object` — ضمایر مفعولی (me, you, him, her, it, us, them)
- ⬜ `en.a1.sentence.negation-basic` — منفی کردن با do/does + not
- ⬜ `en.a1.sentence.question-yes-no` — سوالات بله/خیر با Do/Does
- ⬜ `en.a1.sentence.question-wh` — سوالات wh (who, what, where, when, why, how)
- ⬜ `en.a1.noun.possession-basic` — مالکیت ('s, possessive adjectives)
- ⬜ `en.a1.adjective.basic` — صفات ساده و ترتیب آن‌ها
- ⬜ `en.a1.adverb.frequency-basic` — قیدهای تکرار (always, usually, often, sometimes, never)
- ⬜ `en.a1.verb.imperative-basic` — جملات امری ساده
- ⬜ `en.a1.preposition.basic-time` — حروف اضافه‌ی زمان (at, on, in)
- ⬜ `en.a1.preposition.basic-place` — حروف اضافه‌ی مکان (in, on, under, next to)
- ⬜ `en.a1.noun.numbers-cardinal` — اعداد ۱ تا ۱۰۰
- ⬜ `en.a1.noun.numbers-ordinal` — اعداد ترتیبی (first, second, third...)
- ⬜ `en.a1.verb.past-simple-regular` — گذشته‌ی ساده‌ی افعال باقاعده
- ⬜ `en.a1.verb.past-simple-irregular-common` — گذشته‌ی افعال بی‌قاعده‌ی پرکاربرد
- ⬜ `en.a1.verb.future-will-basic` — آینده با will
- ⬜ `en.a1.verb.future-going-to-basic` — آینده با going to

> ⚠️ قانون: هر گرامر جدید باید حداقل شامل موارد زیر باشد:
> - `base.json` با ID استاندارد، prerequisites معتبر، حداقل ۳ مثال (مثبت/منفی/سوالی در صورت امکان)
> - ترجمه‌ی `name` و `summary` به **هر ۱۱ زبان**
> - ترجمه‌ی `explanation`، `form_notes`، `example_translations`، `common_error_explanations`، `vocab_glosses` به ۱۱ زبان (حداقل en + fa حتماً کامل)
> - حداقل ۳ لغت مرتبط در `content/vocab/en/`
> - حداقل ۱ خطای رایج (common error)

---

## فاز ۲ — تمرین‌ها و اعتبارسنجی پیشرفته

هدف: تولید تمرین‌های متنوع و تقویت validator.

- ⬜ طراحی schema برای `exercises` (grammar-exercise.schema.json)
- ⬜ ایجاد پوشه‌ی `content/exercises/en/a1/` به‌ازای هر grammar point
- ⬜ تولید حداقل ۵ تمرین برای هر گرامر ساخته‌شده (fill-blank, multiple-choice, reorder, error-correction, translation)
- ⬜ گسترش `scripts/validate.py` برای بررسی:
  - اعتبار تمرین‌ها و مطابقت با گرامر
  - وجود audio placeholder برای مثال‌ها
  - consistency بین base و i18n
- ⬜ اسکریپت `scripts/missing_translations.py` برای گزارش ترجمه‌های ناقص به‌ازای هر locale
- ⬜ اسکریپت `scripts/build.py` برای ترکیب base + i18n به خروجی نهایی برای اپ

---

## فاز ۳ — بازبینی توسط native speaker

هدف: تبدیل وضعیت `draft` به `reviewed` و سپس `approved`.

> ⚠️ مهم: هیچ گرامری نباید بدون بازبینی native speaker به وضعیت `published` برسد.

- ⬜ استخدام یا هماهنگی با ۱۱ native linguist (هر زبان یک نفر)
- ⬜ تعریف چک‌لیست بازبینی برای هر گرامر
- ⬜ بازبینی `en.a1.pronoun.personal-subject` توسط nativeها
- ⬜ بازبینی `en.a1.verb.present-simple` توسط nativeها
- ⬜ بازبینی `en.a1.verb.base-form` توسط nativeها
- ⬜ بازبینی لغات ۱۷‌گانه توسط nativeها
- ⬜ تغییر `translation_status` از `draft` به `reviewed` پس از تأیید اولیه
- ⬜ تغییر به `approved` پس از رفع ایرادات
- ⬜ تغییر به `published` پس از اتمام کامل فازهای ۲ و ۴

> 💡 نکته: برای فارسی و عربی، علاوه بر native speaker، یک ویراستار مسلط به نیم‌فاصله و اعراب‌گذاری نیاز است.
> 💡 برای هندی، بررسی تطابق جنسیت در ترجمه‌ها الزامی است.
> 💡 برای ژاپنی، بررسی فرم ます/ません و ذرات (は، が، を) ضروری است.

---

## فاز ۴ — صوت و تلفظ

- ⬜ تعریف ساختار پوشه‌ی `audio/en/a1/...`
- ⬜ تولید یا تهیه‌ی فایل‌های صوتی برای:
  - هر مثال (target_text)
  - هر لغت (lemma)
  - تلفظ نام گرامر
- ⬜ لینک کردن audio_url در base.json و vocab base.json
- ⬜ پشتیبانی از TTS با کیفیت بالا (ElevenLabs یا مشابه) به‌عنوان placeholder تا ضبط نهایی

---

## فاز ۵ — دیتابیس و API

هدف: انتقال داده‌ها از JSON به دیتابیس و ارائه به اپ.

- ⬜ طراحی schema نهایی PostgreSQL (بر اساس ساختار JSON فعلی)
- ⬜ نوشتن migration scripts
- ⬜ اسکریپت `scripts/import_to_db.py`
- ⬜ راه‌اندازی Supabase یا PostgreSQL مستقیم
- ⬜ طراحی API endpoints:
  - `GET /grammar/:id` — دریافت یک گرامر با ترجمه‌ها
  - `GET /grammar?language=en&cefr=A1` — لیست گرامرها
  - `GET /vocab/:id` — دریافت یک لغت با ترجمه‌ها
  - `GET /exercises?grammar_id=...` — تمرین‌های یک گرامر
- ⬜ پشتیبانی از فیلتر locale در درخواست‌ها
- ⬜ caching layer برای کاهش بار

---

## فاز ۶ — گسترش به زبان‌های دیگر (Language Expansion)

هدف: ساخت گرامرهای A1 برای ۱۰ زبان هدف دیگر.

> ⚠️ قانون: تا زمانی که فاز ۱ برای English کامل نشود (۲۰ گرامر A1 + native review)، نباید به زبان‌های دیگر رفت.
> استثنا: می‌توان یک گرامر نمونه برای فارسی (`fa.a1.verb.present-simple`) برای تست RTL و ساختار خاص فارسی ساخت.

- ⬜ ساخت گرامر نمونه فارسی: `fa.a1.verb.present-simple` با فیلدهای اختصاصی (formal/informal, ezafe, colloquial)
- ⬜ ساخت گرامر نمونه عربی: `ar.a1.verb.present-simple` با فیلدهای اختصاصی (root, pattern, gender, dual)
- ⬜ ساخت گرامر نمونه ژاپنی: `ja.a1.verb.present-basic` با فیلدهای اختصاصی (particle, politeness, reading)
- ⬜ ساخت گرامر نمونه ترکی: `tr.a1.verb.genis-zaman` با فیلدهای اختصاصی (vowel harmony, suffix slots)
- ⬜ ساخت گرامر نمونه آلمانی: `de.a1.verb.present` با فیلدهای اختصاصی (case, gender, verb position)
- ⬜ و به همین ترتیب برای es, fr, hi, pt, ru

> 💡 هر زبان جدید نیاز به `config/language-features/{code}.json` برای تعریف فیلدهای اختصاصی آن زبان دارد.

---

## فاز ۷ — سطوح بالاتر (A2 → C2)

- ⬜ تعریف گرامرهای A2 برای English (past continuous, present perfect, comparatives, etc.)
- ⬜ تعریف گرامرهای B1 (passive, conditionals 1&2, reported speech, modals)
- ⬜ تعریف گرامرهای B2 (conditionals 3, subjunctive in Spanish/French, advanced modals)
- ⬜ تعریف گرامرهای C1/C2 (nuance, register, advanced discourse markers)

---

## فاز ۸ — ویژگی‌های اپ

- ⬜ Spaced Repetition System (SRS) برای گرامرها و لغات
- ⬜ Progress tracking با فیلدهای `user_progress` در دیتابیس
- ⬜ Offline support با دانلود بسته‌های گرامر
- ⬜ Search هوشمند با Universal Dependencies tags
- ⬜ Error diagnosis: تشخیص خطاهای کاربر و پیشنهاد گرامر مرتبط
- ⬜ Variant support (pt-BR vs pt-PT, en-US vs en-GB, es-ES vs es-LA)

---

## قوانین طلایی پروژه

1. **کیفیت بر کمیت مقدم است.** هیچ گرامری بدون بازبینی native منتشر نمی‌شود.
2. **هیچ محتوای توهمی تولید نمی‌شود.** اگر نمی‌دانیم، نمی‌نویسیم.
3. **IDها immutable هستند.** بعد از انتشار، ID تغییر نمی‌کند.
4. **متن زبان هدف ترجمه نمی‌شود.** `target_text` همیشه به زبان هدف است، ترجمه در `translations`.
5. **جداسازی base و i18n اجباری است.** داده‌های ساختاری و داده‌های ترجمه‌پذیر جدا نگهداری می‌شوند.
6. **هر گرامر باید حداقل ۳ مثال و ۳ لغت مرتبط داشته باشد.**
7. **هر لغت باید در حداقل یک گرامر reference شود.**
8. **وضعیت محتوا (`status`) و وضعیت ترجمه (`translation_status`) همیشه به‌روز باشند.**
9. **پلن (`plan.md`) باید همیشه بازتاب‌دهنده‌ی وضعیت واقعی پروژه باشد.**
10. **هیچ تغییری نباید بدون آپدیت `README.md` و `plan.md` انجام شود.**

---

## وضعیت فعلی به تفکیک

| دسته | تکمیل‌شده | باقی‌مانده |
|---|---|---|
| گرامرهای English A1 | ۴ | ۱۶ |
| لغات English A1 | ۳۳ | ~۱۱۷ |
| تمرین‌ها | ۰ | ~۱۰۰ |
| بازبینی native | ۰ | همه |
| صوت | ۰ | همه |
| دیتابیس | ۰ | کامل |
| زبان‌های دیگر | ۰ | ۱۰ زبان |
| سطوح بالاتر | ۰ | ۵ سطح |

---

## Dependency Graph گرامرهای ساخته‌شده

```
en.a1.pronoun.personal-subject (✅)
        │
        ├──► en.a1.verb.base-form (✅)
        │         │
        │         ▼
        │    en.a1.verb.present-simple (✅)
        │
        └──► en.a1.verb.copula-basic (✅)
```

---

## قدم بعدی پیشنهادی

۱. اجرای `python3 scripts/validate.py` برای اطمینان از سلامت وضعیت فعلی.
۲. ساخت گرامر بعدی: **`en.a1.noun.definiteness-basic`** (حروف تعریف a/an/the)
   - چون پیش‌نیاز مستقیم copula-basic است (در مثال I am a student)
   - یکی از سخت‌ترین مفاهیم برای فارسی‌زبانان (که حرف تعریف ندارند)
   - نیاز به لغات جدید: cat, dog, car, house, city, country, language, person
۳. پس از ساخت، آپدیت این فایل با ✅.
۴. تکرار تا تکمیل فاز ۱.

---

## تاریخچه‌ی تغییرات این فایل

- **2026-08-04**: ایجاد اولیه، بازتاب دقیق وضعیت فعلی پروژه (۲ گرامر، ۹ لغت، فاز ۰ کامل، فاز ۱ در حال انجام).
- **2026-08-04**: تکمیل گرامر `en.a1.verb.base-form` با ترجمه‌ی کامل ۱۱ زبانه و افزودن ۸ لغت جدید (like, want, have, do, go, eat, see, come).
- **2026-08-04**: تکمیل گرامر `en.a1.verb.copula-basic` با ترجمه‌ی کامل ۱۱ زبانه و افزودن ۸ لغت جدید (be, happy, sad, tired, hungry, home, school, work-noun).
