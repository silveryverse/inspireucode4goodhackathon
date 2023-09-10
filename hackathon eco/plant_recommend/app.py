from flask import Flask, render_template, request
import pandas as pd
app = Flask(__name__, static_url_path='/static')


# Load the dataset
data = pd.read_csv('plant_data_with_tags.csv')

# Get unique tags from the dataset
unique_tags = data['tag'].unique()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        plant_type = request.form['plant_type'].strip().lower()
        total_budget = float(request.form['total_budget'])
        total_plants = int(request.form['total_plants'])

        recommended_plants_by_tag = {}

        if plant_type != 'combo' and plant_type not in unique_tags:
            error_message = f"Sorry, '{plant_type}' is not a valid plant type."
            return render_template('index.html', recommended_plants={}, error_message=error_message)

        budget_per_tag = total_budget / len(unique_tags) if plant_type == 'combo' else total_budget

        if plant_type == 'combo':
            recommended_plants = []

            for tag in unique_tags:
                filtered_data = data[data['tag'] == tag]
                affordable_plants = filtered_data[filtered_data['price'] <= budget_per_tag].drop_duplicates(subset=['common_name'])

                if not affordable_plants.empty:
                    num_plants_to_select = min(5, len(affordable_plants))
                    selected_plants = affordable_plants.sample(n=num_plants_to_select)
                    recommended_plants.extend(selected_plants.iterrows())

            recommended_plants_by_tag = {tag.capitalize(): [] for tag in unique_tags}

            for _, row in recommended_plants:
                recommended_plants_by_tag[row['tag'].capitalize()].append({
                    'Common Name': row['common_name'],
                    'Hindi Name': row['hindi_name'],
                    'Price': f'{row["price"]:.2f}'
                })

        else:
            filtered_data = data[data['tag'] == plant_type]
            sorted_data = filtered_data.sort_values(by='price', ascending=True)
            affordable_plants = sorted_data[sorted_data['price'] <= total_budget].drop_duplicates(subset=['common_name'])
            recommended_plants_by_tag[plant_type.capitalize()] = []

            for index, row in affordable_plants.head(total_plants).iterrows():
                recommended_plants_by_tag[plant_type.capitalize()].append({
                    'Common Name': row['common_name'],
                    'Hindi Name': row['hindi_name'],
                    'Price': f'{row["price"]:.2f}'
                })

        return render_template('index.html', recommended_plants=recommended_plants_by_tag)

    return render_template('index.html', recommended_plants={}, error_message=None)

if __name__ == '__main__':
    app.run(debug=True, port=8001)