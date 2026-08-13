# MedIntel AI - Database Design

## 1. Purpose

The MedIntel AI database stores structured information required for
longitudinal medical document analysis.

The system separates:

1. Raw document information
2. Extracted medical observations
3. Processing state
4. Derived AI analysis

The database is not intended to make autonomous medical diagnoses.

---

## 2. Core Entities

The initial database contains five core entities:

- Patients
- Documents
- Observations
- Processing Jobs
- AI Analyses

---

## 3. Entity Relationship Overview

```text
Patient
  |
  +---- Documents
  |        |
  |        +---- Processing Jobs
  |        |
  |        +---- Observations
  |
  +---- AI Analyses
  ---

## 4. Patients

Represents an internal patient record.

### Fields

| Field | Type | Description |
|---|---|---|
| id | UUID | Primary identifier |
| created_at | TIMESTAMP | Record creation time |
| updated_at | TIMESTAMP | Last modification time |

The prototype intentionally avoids storing unnecessary personally
identifiable information.

---

## 5. Documents

Represents an uploaded medical document.

### Fields

| Field | Type | Description |
|---|---|---|
| id | UUID | Primary identifier |
| patient_id | UUID | Associated patient |
| original_filename | VARCHAR | Original uploaded filename |
| document_type | VARCHAR | Type of medical document |
| report_date | DATE | Date associated with the report |
| storage_path | TEXT | Location of stored document |
| mime_type | VARCHAR | Document MIME type |
| file_size | BIGINT | File size in bytes |
| processing_status | VARCHAR | Current processing state |
| created_at | TIMESTAMP | Upload/record creation time |
| updated_at | TIMESTAMP | Last modification time |

The actual document file is stored outside the relational database.

---

## 6. Observations

Observations are the core structured medical data used for
longitudinal analysis.

### Fields

| Field | Type | Description |
|---|---|---|
| id | UUID | Primary identifier |
| document_id | UUID | Source document |
| patient_id | UUID | Associated patient |
| test_name | VARCHAR | Original extracted test name |
| normalized_test_name | VARCHAR | Canonical test name |
| value_numeric | NUMERIC | Numeric result when available |
| value_text | TEXT | Text result when applicable |
| unit | VARCHAR | Measurement unit |
| reference_low | NUMERIC | Lower numeric reference limit |
| reference_high | NUMERIC | Upper numeric reference limit |
| reference_text | TEXT | Non-numeric reference information |
| observed_at | DATE | Date of observation |
| abnormal_flag | VARCHAR | Reported or derived abnormality state |
| source_text | TEXT | Original text supporting extraction |
| confidence | NUMERIC | Extraction confidence |
| created_at | TIMESTAMP | Record creation time |

### Example

```text
test_name: Hemoglobin
normalized_test_name: hemoglobin
value_numeric: 12.4
unit: g/dL
reference_low: 12.0
reference_high: 16.0
observed_at: 2025-08-12---

## 8. AI Analyses

Stores generated analysis and model metadata.

### Fields

| Field | Type | Description |
|---|---|---|
| id | UUID | Primary identifier |
| patient_id | UUID | Associated patient |
| analysis_type | VARCHAR | Type of analysis |
| model_provider | VARCHAR | AI provider |
| model_name | VARCHAR | Model used |
| input_context_hash | VARCHAR | Identifier for analyzed context |
| result | TEXT | Generated analysis |
| created_at | TIMESTAMP | Analysis creation time |

The AI analysis layer explains structured information produced by the
system rather than acting as an autonomous diagnostic system.

---

## 9. Relationships

### Patient -> Documents

One patient can have multiple medical documents.

### Document -> Observations

One document can contain multiple medical observations.

### Document -> Processing Jobs

One document can have multiple processing jobs.

### Patient -> AI Analyses

One patient can have multiple generated analyses.

---

## 10. Data Processing Architecture

```text
Uploaded Document
       |
       v
Document Storage
       |
       v
Text Extraction
       |
       v
OCR when required
       |
       v
Medical Information Extraction
       |
       v
Normalization
       |
       v
Structured Observations
       |
       v
Trend Analysis
       |
       v
Attention Signals
       |
       v
AI Explanation