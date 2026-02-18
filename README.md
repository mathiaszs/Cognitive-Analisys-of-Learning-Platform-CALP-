# CALP — Cognitive Analisys of Learning Platform
Learning Behavior Capture API

This API records raw study behavior data for cognitive learning analysis.

## Stack
- FastAPI
- SQLite
- SQLAlchemy

## Run

uvicorn main:app --reload

## Endpoints

POST /sessions → creates a study session
POST /events → logs behavioral data

## Purpose

Provide structured datasets for modeling learning curves,
attention decay, and retention patterns.
