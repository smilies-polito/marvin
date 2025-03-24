import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Load datasets
all_invalidate_file = "all_invalidate.csv"
no_invalidate_file = "no_invalidate.csv"
cache_invalidate_file = "cache_invalidate.csv"
tlb_bpa_invalidate_file = "tlb_bpa_invalidate.csv"

cache_df = pd.read_csv(all_invalidate_file)
no_cache_df = pd.read_csv(no_invalidate_file)
only_cache_df = pd.read_csv(cache_invalidate_file)
tlb_bpa_df = pd.read_csv(tlb_bpa_invalidate_file)  # Load the fourth dataset

# Select relevant features (skip first 7 columns and last column)
def extract_features(df):
    return df.iloc[:, 7:-1]

cache_features = extract_features(cache_df)
no_cache_features = extract_features(no_cache_df)
only_cache_features = extract_features(only_cache_df)
tlb_bpa_features = extract_features(tlb_bpa_df)  # Extract features for the new dataset

# Convert all data to numeric and drop NaN values
cache_features = cache_features.apply(pd.to_numeric, errors='coerce').dropna()
no_cache_features = no_cache_features.apply(pd.to_numeric, errors='coerce').dropna()
only_cache_features = only_cache_features.apply(pd.to_numeric, errors='coerce').dropna()
tlb_bpa_features = tlb_bpa_features.apply(pd.to_numeric, errors='coerce').dropna()  # Clean fourth dataset

# Remove rows containing decimal values
cache_features = cache_features[(cache_features % 1 == 0).all(axis=1)]
no_cache_features = no_cache_features[(no_cache_features % 1 == 0).all(axis=1)]
only_cache_features = only_cache_features[(only_cache_features % 1 == 0).all(axis=1)]
tlb_bpa_features = tlb_bpa_features[(tlb_bpa_features % 1 == 0).all(axis=1)]  # Clean fourth dataset

# Assign labels
cache_features["label"] = "Standard"
no_cache_features["label"] = "No Invalidation"
only_cache_features["label"] = "Cache only Invalidation"
tlb_bpa_features["label"] = "Tlb and Bpa only Invalidation"  # New label

# Combine datasets
dataset = pd.concat([cache_features, no_cache_features, only_cache_features, tlb_bpa_features], ignore_index=True)

# Extract feature values and drop NaNs
features = dataset.drop(columns=["label"]).dropna()

# Standardize features
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

# Apply PCA
pca = PCA(n_components=2)
pca_result = pca.fit_transform(scaled_features)

# Convert to DataFrame for plotting
pca_df = pd.DataFrame(pca_result, columns=["PC1", "PC2"])
pca_df["label"] = dataset["label"].values[:len(pca_df)]

# Plot PCA results
plt.figure(figsize=(8, 6))
colors = {
    "Standard": "green",
    "No Invalidation": "blue",
    "Cache only Invalidation": "red",
    "Tlb and Bpa only Invalidation": "purple"
}  # Update color mapping

for label in colors:
    subset = pca_df[pca_df["label"] == label]
    plt.scatter(subset["PC1"], subset["PC2"], label=label, color=colors[label], alpha=0.6)

plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("PCA Scatter Plot of Invalidation Types")
plt.legend()
plt.show()

# Plot histograms for each of the features, 6 at a time
num_features = features.shape[1]
features_per_plot = 6  # Number of features per figure

for start in range(0, num_features, features_per_plot):
    end = min(start + features_per_plot, num_features)
    fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(15, 10))
    axes = axes.flatten()

    for i, feature_idx in enumerate(range(start, end)):
        axes[i].hist(cache_features.iloc[:, feature_idx], bins=30, alpha=0.5, color='green', edgecolor='black', label='Standard')
        axes[i].hist(no_cache_features.iloc[:, feature_idx], bins=30, alpha=0.5, color='blue', edgecolor='black', label='No Invalidation')
        axes[i].hist(only_cache_features.iloc[:, feature_idx], bins=30, alpha=0.5, color='red', edgecolor='black', label='Cache only Invalidation')
        axes[i].hist(tlb_bpa_features.iloc[:, feature_idx], bins=30, alpha=0.5, color='purple', edgecolor='black', label='Tlb and Bpa Invalidation')
        axes[i].set_title(f'Feature {feature_idx + 1}')
        axes[i].legend()

    # Remove any unused subplots
    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])

    plt.tight_layout()
    plt.show()