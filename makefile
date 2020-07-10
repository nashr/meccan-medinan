get_dataset: src/data/get_raw_data.py
	python src/data/get_raw_data.py

build_feature: src/features/build_feature.py
	python src/features/build_feature.py

build_tree: src/models/build_decision_tree.py
	python src/models/build_decision_tree.py
