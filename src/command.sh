# python3 artistDataCleaner.py
# python3 extract_tags.py
# python3 Input_read.py ../src/Concept_hierarchy_for_artist_datasets.txt ../src/clean_artist_CH.txt
# python3 Calculating_drank.py ../src/clean_artist_CH.txt ../src/rules.txt > Drank_for_artists_datasets.txt
# python3 arrange_confidence_and_drank_ARs.py ../src/rules.txt ../src/Drank_for_artist_datasets.txt
# echo "../Artist_experiment/Datasets/test_data.txt" | python3 make_recommendations.py > Recommendations.txt
python3 Calculating_drank.py ../src/clean_artist_CH.txt ../src/test_rules.txt > Drank_for_test_artists.txt
