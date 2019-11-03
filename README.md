# Improving-Diversity-Performance-of-Association-Rule-Based-Recommender-Systems

### Note that the dataset has been moved to movielense-experiment folder.

Order of running the files to run the code:
- src/movielensdataCleaner.py
  -- takes movielens data as input
  -- gives out frequent patterns and association rules (by confidence)
- src/main_1.py
  -- finds the dranks for all patterns constructed from association rules
- src/arrange_confidence_and_drank_ARs.py
  -- sorts both association rules based on confidence and drank
- src/make_recommendations.py
  -- takes input file as patterns for which to recommend
  -- gives out recommendations.
