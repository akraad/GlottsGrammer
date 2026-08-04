# GlottsGrammer

Source-of-truth content repository for a multi-lingual grammar system.
The data here is the single authoritative copy used by the language app across 11 target languages:

- `ar` Arabic
- `de` German
- `en` English
- `es` Spanish
- `fa` Persian (Farsi)
- `fr` French
- `hi` Hindi
- `ja` Japanese
- `pt` Portuguese
- `ru` Russian
- `tr` Turkish

## Directory layout

```
GlottsGrammer/
├── config/                 # reference data shared by every grammar point
│   ├── locales.json
│   ├── levels.json
│   ├── categories.json
│   └── universal-concepts.json
├── schemas/                # JSON Schema (draft-07) for every content type
│   ├── grammar-base.schema.json
│   ├── grammar-i18n.schema.json
│   ├── vocab-base.schema.json
│   └── vocab-i18n.schema.json
├── content/
│   ├── grammar/{lang}/{cefr}/{category}/{slug}/
│   │   ├── base.json                       # structure, not translated
│   │   └── i18n/{locale}.json              # translated metadata per locale
│   └── vocab/{lang}/{lemma}/
│       └── base.json                       # vocab with translations inline
└── scripts/
    └── validate.py         # structural + cross-reference validator
```

## Conventions

### Grammar point IDs

Format:

```
{target_language}.{cefr}.{category}.{slug}
```

Rules:
- lowercase ASCII only
- hyphens instead of spaces
- IDs are immutable once published

Examples:
- `en.a1.verb.present-simple`
- `en.a1.pronoun.personal-subject`
- `en.a1.verb.base-form`

### Vocabulary IDs

Format:

```
{language}.{pos}.{lemma-slug}
```

Examples:
- `en.verb.drink`
- `en.noun.water`
- `en.phrase.every-day`
- `en.verb.have`
- `en.verb.do`

### Separation of structural vs. translated data

Grammar points are split into two files on purpose:

- `base.json` holds data that must **never** be translated (IDs, forms, target-language example sentences, vocab references, prerequisites).
- `i18n/{locale}.json` holds data that **must** be translated (name, summary, explanation, form notes, example translations, error explanations, vocab glosses).

This prevents accidental translation of target-language examples and keeps the repository diff-friendly.

### Translation status

Every `i18n/*.json` file carries a `translation_status` field:

```
draft | translated | reviewed | approved | published
```

A grammar point is considered **ready for release** only when every locale is at least `reviewed`.

## Validation

Run from the repository root:

```bash
python3 scripts/validate.py
```

The script checks:

1. All config JSON files parse.
2. Every grammar `base.json` has all required fields.
3. Every vocab `base.json` has all required fields.
4. Language, CEFR level, and universal concept references exist in config.
5. Every vocab reference in a grammar point points to an existing vocab ID.
6. Every grammar point has an `i18n/` directory with a JSON file for each configured locale.
7. Each i18n file declares the locale it claims to represent.
8. Each i18n file has `example_translations` for every example in base.
9. Each i18n file has `common_error_explanations` for every error in base.
10. Each i18n file has `vocab_glosses` for every vocab reference in base.
11. All prerequisite references point to existing grammar points.

## Current state

The repository currently contains:

### Config & Schemas
- Full config files (locales, levels, categories, universal concepts).
- JSON Schemas for grammar base, grammar i18n, vocab base, vocab i18n.
- A working Python validator with cross-reference checks.

### Grammar Points (3 total)

1. **English A1 Present Simple** (`en.a1.verb.present-simple`)
   - Full base with 3 forms (affirmative/negative/question), 3 examples, 1 common error
   - Translations for all 11 locales (status: `draft`)
   - 3 supporting vocab items: `drink`, `water`, `every-day`
   - Prerequisites: `en.a1.pronoun.personal-subject`, `en.a1.verb.base-form`

2. **English A1 Subject Pronouns** (`en.a1.pronoun.personal-subject`)
   - Full base with 2 forms (singular/plural), 3 examples, 2 common errors
   - Translations for all 11 locales (status: `draft`)
   - 7 supporting vocab items: `student`, `friend`, `book`, `teacher`, `tea`, `work`, `drink`
   - Prerequisites: none (root grammar point)

3. **English A1 Verb Base Form** (`en.a1.verb.base-form`)
   - Full base with 3 forms (affirmative base, negative with does, question with do), 3 examples, 2 common errors
   - Translations for all 11 locales (status: `draft`)
   - 11 supporting vocab items: `drink`, `water`, `tea`, `like`, `want`, `have`, `do`, `go`, `eat`, `see`, `come`
   - Prerequisites: `en.a1.pronoun.personal-subject`

### Vocabulary (17 items)

**Nouns:**
- `en.noun.water` — آب / Wasser / eau / 水
- `en.noun.tea` — چای / Tee / thé / お茶
- `en.noun.student` — دانش‌آموز / Schüler / étudiant / 学生
- `en.noun.friend` — دوست / Freund / ami / 友達
- `en.noun.book` — کتاب / Buch / livre / 本
- `en.noun.teacher` — معلم / Lehrer / professeur / 先生

**Verbs:**
- `en.verb.drink` — نوشیدن / trinken / boire / 飲む
- `en.verb.work` — کار کردن / arbeiten / travailler / 働く
- `en.verb.like` — دوست داشتن / mögen / aimer / 好きである
- `en.verb.want` — خواستن / wollen / vouloir / 望む
- `en.verb.have` — داشتن / haben / avoir / 持っている
- `en.verb.do` — انجام دادن / tun / faire / する
- `en.verb.go` — رفتن / gehen / aller / 行く
- `en.verb.eat` — خوردن / essen / manger / 食べる
- `en.verb.see` — دیدن / sehen / voir / 見る
- `en.verb.come` — آمدن / kommen / venir / 来る

**Phrases:**
- `en.phrase.every-day` — هر روز / jeden Tag / tous les jours / 毎日

## Dependency Graph

```
en.a1.pronoun.personal-subject
        │
        ▼
en.a1.verb.base-form
        │
        ▼
en.a1.verb.present-simple
```

## Next steps

1. **Native speaker review** - All translations are currently in `draft` status and need review by native speakers of each language.
2. **Expand A1 content** - Build out the remaining A1 grammar points following the dependency graph:
   - `en.a1.verb.copula-basic` (to be: am/is/are)
   - `en.a1.noun.basic-plural` (singular/plural)
   - `en.a1.sentence.negation-basic` (basic negation)
   - `en.a1.sentence.question-yes-no` (yes/no questions)
   - etc.
3. **Add exercises** - Each grammar point needs exercises (fill-blank, multiple choice, reorder, error correction).
4. **Add audio** - Record audio for all example sentences.

## Quality notes

All translations were generated programmatically and **have not yet been reviewed by native speakers**. Before publishing any grammar point, ensure:

- [ ] Every `i18n/*.json` has been reviewed by a native speaker of that language
- [ ] Example translations are natural and accurate
- [ ] Form notes correctly describe the grammar in the target language
- [ ] Common error explanations are culturally and linguistically appropriate
- [ ] Vocab glosses match the context in which they appear
- [ ] Translation status is updated to `reviewed` or `approved` after review
