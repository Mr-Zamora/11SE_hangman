# 📊 Data Dictionary

## Overview
This document defines all key variables, data structures, and constants used in the Hangman game.

## 🔤 Variables

### Game State Variables
| Variable | Type | Purpose | Example |
|----------|------|---------|---------|
| current_word | string | The word player needs to guess | "python" |
| guessed_letters | set | Collection of letters already guessed | {"p", "y", "n"} |
| score | integer | Current player score | 80 |
| difficulty | string | Selected game difficulty | "medium" |

### Game Settings
| Constant | Type | Value | Purpose |
|----------|------|--------|---------|
| MAX_SCORE | integer | 100 | Starting score for each game |
| HINT_THRESHOLD | integer | 3 | Number of wrong guesses before hint |

### Data Structures
| Structure | Type | Contents | Purpose |
|-----------|------|----------|---------|
| DIFFICULTY_WORDS | dict | {"easy": [...], "medium": [...]} | Word lists by difficulty |

## 🔍 Function Parameters

### display_word()
| Parameter | Type | Purpose |
|-----------|------|---------|
| word | string | The target word |
| guessed_letters | set | Letters guessed so far |

### get_hint()
| Parameter | Type | Purpose |
|-----------|------|---------|
| word | string | The target word |
| guessed_letters | set | Letters already guessed |

## 📝 Implementation Notes
- Document any new variables added
- Include valid value ranges
- Note any dependencies
- Explain data type choices
