import os
import random
import shutil


def split_dataset(train_dir, test_dir, test_ratio=0.4, seed=None):
    """
    Splits a dataset by moving a proportion of files from each label folder in train_dir
    to a corresponding folder in test_dir.

    :param train_dir: Path to the training data directory containing label subfolders.
    :param test_dir: Path to the output test data directory.
    :param test_ratio: Fraction of files to move to test (e.g., 0.4 for 40%).
    :param seed: Optional random seed for reproducibility.
    """
    if seed is not None:
        random.seed(seed)

    # Iterate over each label folder
    for label in os.listdir(train_dir):
        label_dir = os.path.join(train_dir, label)
        if not os.path.isdir(label_dir):
            continue

        # Create corresponding test label folder
        test_label_dir = os.path.join(test_dir, label)
        os.makedirs(test_label_dir, exist_ok=True)

        # List all files in the label directory
        files = [f for f in os.listdir(label_dir)
                 if os.path.isfile(os.path.join(label_dir, f))]

        # Determine number of test samples
        n_test = int(len(files) * test_ratio)
        if n_test == 0:
            continue

        # Randomly sample files for test set
        test_files = random.sample(files, n_test)

        # Move each selected file to the test directory
        for filename in test_files:
            src_path = os.path.join(label_dir, filename)
            dst_path = os.path.join(test_label_dir, filename)
            shutil.move(src_path, dst_path)
            print(f"Moved: {src_path} --> {dst_path}")


if __name__ == "__main__":
    # Define the source and destination directories
    train_dir = r"C:\Python_Codes\FaceExpCPE620\datasets\manga\train"
    test_dir = r"C:\Python_Codes\FaceExpCPE620\datasets\manga\test"

    print('Splitting dataset...')
    # Perform the split (40% to test, 60% remains in train)
    split_dataset(train_dir, test_dir, test_ratio=0.4, seed=42)
    print('Dataset split completed.')
    
