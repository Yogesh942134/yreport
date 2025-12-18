# Data Health Report

## Summary
- **Health Score:** 89.56/100
- **Rows:** 950
- **Columns:** 20

## Column Types
- **Numeric**: ['ID', 'Margin']
- **Categorical**: ['City', 'Date', 'Season', 'MatchNumber', 'Team1', 'Team2', 'Venue', 'TossWinner', 'TossDecision', 'SuperOver', 'WinningTeam', 'WonBy', 'method', 'Player_of_Match', 'Team1Players', 'Team2Players', 'Umpire1', 'Umpire2']
- **Datetime**: []

## Missing Percentage
- **City**: 5.37%
- **SuperOver**: 0.42%
- **WinningTeam**: 0.42%
- **Margin**: 1.89%
- **method**: 98.0%
- **Player_of_Match**: 0.42%

## Warnings
- **high_missing**: ['method']
- **high_cardinality**: ['Date', 'MatchNumber', 'Player_of_Match', 'Team1Players', 'Team2Players', 'Umpire1', 'Umpire2']

## Recommendations
### Encoding
- **City**: Categorical encoding required (Confidence: MEDIUM)
- **Date**: Categorical encoding required (high cardinality) (Confidence: HIGH)
- **Season**: Categorical encoding required (Confidence: MEDIUM)
- **MatchNumber**: Categorical encoding required (high cardinality) (Confidence: HIGH)
- **Team1**: Categorical encoding required (Confidence: MEDIUM)
- **Team2**: Categorical encoding required (Confidence: MEDIUM)
- **Venue**: Categorical encoding required (Confidence: MEDIUM)
- **TossWinner**: Categorical encoding required (Confidence: MEDIUM)
- **TossDecision**: Categorical encoding required (Confidence: MEDIUM)
- **SuperOver**: Categorical encoding required (Confidence: MEDIUM)
- **WinningTeam**: Categorical encoding required (Confidence: MEDIUM)
- **WonBy**: Categorical encoding required (Confidence: MEDIUM)
- **Player_of_Match**: Categorical encoding required (high cardinality) (Confidence: HIGH)
- **Team1Players**: Categorical encoding required (high cardinality) (Confidence: HIGH)
- **Team2Players**: Categorical encoding required (high cardinality) (Confidence: HIGH)
- **Umpire1**: Categorical encoding required (high cardinality) (Confidence: HIGH)
- **Umpire2**: Categorical encoding required (high cardinality) (Confidence: HIGH)

### Missing Values
- **City**: impute (5.37% missing values, Confidence: MEDIUM)
- **method**: drop (98.0% missing values, Confidence: HIGH)

## Numeric Diagnostics
- **ID**: skew=0.0, outliers=0.0%, no transform needed
- **Margin**: skew=2.65, outliers=12.23%, consider log/robust transform