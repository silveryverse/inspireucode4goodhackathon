import pandas as pd
import random
import pickle

# Load the dataset
data = pd.read_csv('plant_data_with_tags.csv')

# Get unique tags from the dataset
unique_tags = data['tag'].unique()

# Input parameters from the user
print("Available plant types:")
print(", ".join(unique_tags))

plant_type = input("Enter 'combo' to get a mix of all plant types or choose a specific tag (flower, indoor, herb, fruit, vegetable): ").strip().lower()

# Check if the user wants a combo or a single type
if plant_type != 'combo' and plant_type not in unique_tags:
    print(f"Sorry, {plant_type} is not a valid plant type.")
else:
    if plant_type == 'combo':
        total_budget = float(input("Enter your total budget (should be more than 1000): "))
        while total_budget <= 1000:
            total_budget = float(input("Please enter a budget higher than 1000: "))
        total_plants = int(input("Enter the total number of plants you want: "))
    else:
        total_budget = float(input("Enter your total budget: "))
        total_plants = int(input("Enter the total number of plants you want: "))

    # Initialize a dictionary to store recommended plants by tag
    recommended_plants_by_tag = {}

    # Calculate the budget per tag
    budget_per_tag = total_budget / len(unique_tags) if plant_type == 'combo' else total_budget

    # Check if the user wants a combo of plants
    if plant_type == 'combo':
        recommended_plants = []

        # Iterate through tags and recommend at least 5 plants from each tag
        for tag in unique_tags:
            filtered_data = data[data['tag'] == tag]
            affordable_plants = filtered_data[filtered_data['price'] <= budget_per_tag].drop_duplicates(subset=['common_name'])

            # Check if there are affordable plants for this tag
            if not affordable_plants.empty:
                # Ensure at least 5 plants from each tag
                num_plants_to_select = min(5, len(affordable_plants))
                selected_plant = affordable_plants.sample(n=num_plants_to_select)
                recommended_plants.extend(selected_plant.index)

        # Retrieve the selected plants from the dataset
        selected_plants_data = data.loc[recommended_plants]

        # Group selected plants by tag
        selected_plants_by_tag = selected_plants_data.groupby('tag')

        # Create a list to store recommended plants
        recommended_plants_list = []

        # Display the recommended plants by tag
        for tag, plants in selected_plants_by_tag:
            for index, row in plants.iterrows():
                recommended_plants_list.append((tag.capitalize(), row['common_name'], row['hindi_name'], row['price']))

        # Save the recommended plants to a pickle file
        with open('recommended_plants.pkl', 'wb') as f:
            pickle.dump(recommended_plants_list, f)

        print("Recommended plants have been saved to 'recommended_plants.pkl'.")

    else:
        # Filter the dataset based on the user's plant type
        filtered_data = data[data['tag'] == plant_type]

        # Sort the filtered data by price in ascending order
        sorted_data = filtered_data.sort_values(by='price', ascending=True)

        # Find the plants that fit within the total budget for the selected type and are distinct
        affordable_plants = sorted_data[sorted_data['price'] <= total_budget].drop_duplicates(subset=['common_name'])

        # Limit the number of plants based on the user's input
        affordable_plants = affordable_plants.head(total_plants)
        recommended_plants_by_tag[plant_type] = affordable_plants

        # Create a list to store recommended plants
        recommended_plants_list = []

        # Display the recommended plants by tag
        for tag, plants in recommended_plants_by_tag.items():
            for index, row in plants.iterrows():
                recommended_plants_list.append((tag.capitalize(), row['common_name'], row['hindi_name'], row['price']))

        # Save the recommended plants to a pickle file
        with open('recommended_plants.pkl', 'wb') as f:
            pickle.dump(recommended_plants_list, f)

        print("Recommended plants have been saved to 'recommended_plants.pkl'.")
