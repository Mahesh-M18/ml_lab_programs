import pandas as pd
import numpy as np

# Load dataset
dataset = pd.read_csv("playtennis.csv", names=["outlook", "temperature", "humidity", "wind", "class"])

# --- Step 1: Entropy ---
def entropy(target_col):
    elements, counts = np.unique(target_col, return_counts=True)
    return np.sum([(-counts[i]/np.sum(counts)) * np.log2(counts[i]/np.sum(counts)) for i in range(len(elements))])

# --- Step 2: Information Gain ---
def InfoGain(data, split_attribute_name, target_name="class"):
    total_entropy = entropy(data[target_name])
    vals, counts = np.unique(data[split_attribute_name], return_counts=True)
    Weighted_Entropy = np.sum([(counts[i]/np.sum(counts)) * entropy(data.where(data[split_attribute_name]==vals[i]).dropna()[target_name]) for i in range(len(vals))])
    return total_entropy - Weighted_Entropy

# --- Step 3: ID3 Algorithm ---
def ID3(data, originaldata, features, target_attribute_name="class", parent_node_class=None):
    # If all target values are same → return that value
    if len(np.unique(data[target_attribute_name])) <= 1:
        return np.unique(data[target_attribute_name])[0]
    
    # If dataset empty → return majority value from original dataset
    elif len(data) == 0:
        return np.unique(originaldata[target_attribute_name])[np.argmax(np.unique(originaldata[target_attribute_name], return_counts=True)[1])]
    
    # If no features left → return parent node class (majority)
    elif len(features) == 0:
        return parent_node_class
    
    else:
        # Majority class of current node
        parent_node_class = np.unique(data[target_attribute_name])[np.argmax(np.unique(data[target_attribute_name], return_counts=True)[1])]
        
        # Select best feature
        item_values = [InfoGain(data, feature, target_attribute_name) for feature in features]
        best_feature_index = np.argmax(item_values)
        best_feature = features[best_feature_index]
        
        # Build tree
        tree = {best_feature: {}}
        
        # Remove best feature from list
        remaining_features = [i for i in features if i != best_feature]
        
        # Grow branches
        for value in np.unique(data[best_feature]):
            sub_data = data.where(data[best_feature] == value).dropna()
            subtree = ID3(sub_data, dataset, remaining_features, target_attribute_name, parent_node_class)
            tree[best_feature][value] = subtree
        
        return tree

# --- Step 4: Prediction ---
def predict(query, tree, default=1):
    for key in list(query.keys()):
        if key in list(tree.keys()):
            try:
                result = tree[key][query[key]]
            except:
                return default
            
            if isinstance(result, dict):
                return predict(query, result)
            else:
                return result

# --- Step 5: Train & Test ---
def train_test_split(dataset):
    training_data = dataset.iloc[:14].reset_index(drop=True)  # first 14 rows for training
    return training_data

def test(data, tree):
    queries = data.iloc[:, :-1].to_dict(orient="records")
    predicted = pd.DataFrame(columns=["predicted"])
    for i in range(len(data)):
        predicted.loc[i, "predicted"] = predict(queries[i], tree, 1.0)
    accuracy = np.sum(predicted["predicted"] == data["class"]) / len(data) * 100
    print(f"Prediction Accuracy: {accuracy:.2f}%")

# --- Run ---
training_data = train_test_split(dataset)
tree = ID3(training_data, training_data, training_data.columns[:-1])
print("\nDecision Tree:\n", tree)

# Test accuracy
test(training_data, tree)

# Classify new sample
sample = {'outlook': 0, 'temperature': 1, 'humidity': 1, 'wind': 1}
print("\nPrediction for new sample:", predict(sample, tree))
