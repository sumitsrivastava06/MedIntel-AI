# MedIntel AI

## AI-Powered Longitudinal Medical Intelligence Platform

MedIntel AI is an AI/ML-powered platform designed to analyze a patient's medical reports across multiple time periods, organize extracted medical information into a longitudinal timeline, identify measurable trends, and provide evidence-grounded insights.

The platform is designed as an educational and research-oriented prototype and is **not intended to diagnose diseases, prescribe treatment, or replace qualified medical professionals**.

---

## Problem

Medical information is often distributed across multiple reports, dates, laboratories, and healthcare providers.

Reviewing years of medical reports manually can make it difficult to:

- Track changes over time
- Identify trends in laboratory values
- Locate important information
- Compare historical reports
- Understand how medical information has evolved

---

## Proposed Solution

MedIntel AI aims to provide a centralized system that can:

1. Process uploaded medical documents.
2. Extract relevant medical information.
3. Organize information chronologically.
4. Visualize longitudinal trends.
5. Detect potentially notable changes.
6. Generate evidence-grounded explanations.
7. Provide a RAG-based medical information assistant.
8. Help users discover relevant healthcare resources.

---

## Core Technologies

The project is planned to explore:

- Python
- FastAPI
- React
- TypeScript
- PostgreSQL
- OCR
- NLP
- Machine Learning
- Retrieval-Augmented Generation (RAG)
- Large Language Models (LLMs)
- External APIs
- Optional local LLM inference

The exact technology choices may evolve during development based on technical evaluation and project requirements.

---

## Project Status

**Current Stage:** Phase 1 — Development Environment & Repository Setup

This project is being developed individually as a final-year academic major project.

---

## Planned Architecture

```text
Medical Documents
       |
       v
Document Processing
       |
       v
OCR / Text Extraction
       |
       v
Medical Information Extraction
       |
       v
Longitudinal Timeline
       |
       +-----------> Trend Analysis
       |
       +-----------> Attention Detection
       |
       +-----------> RAG / AI Assistant
       |
       v
Web Dashboard
       |
       +-----------> Healthcare Resource Finder