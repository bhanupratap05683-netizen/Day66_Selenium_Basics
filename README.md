# Day 66: Web Automation Fundamentals with Selenium

## Overview
This repository contains the Day 66 deliverables for the 84-Day Python & Advanced Excel Mastery roadmap. The focus of this module is establishing the foundational architecture for web automation and dynamic data extraction using Selenium WebDriver.

## Technical Objectives
* Successfully configure and initialize the Selenium WebDriver for Python.
* Programmatically navigate to live financial market indices.
* Control browser state (window maximization, session termination) via code.
* Extract top-level DOM elements (Page Title, URL) to verify automated connections.

## Tools & Libraries Used
* **Language:** Python 3.x
* **Library:** `selenium`
* **Driver:** Chrome WebDriver
* **Target Data:** Live financial market indices (Yahoo Finance)

## Business Context
Manual data aggregation is inefficient. This module establishes the base infrastructure required to build autonomous scrapers for financial applications (such as OmniTrade Pro). By automating browser navigation, we bypass the limitations of static HTML scraping, allowing for the extraction of dynamic, JavaScript-rendered market data.

## Execution
To run the automation script:
```bash
pip install selenium
python day66_selenium_intro.py
