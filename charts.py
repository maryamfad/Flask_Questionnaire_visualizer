import matplotlib.pyplot as plt
import os
import uuid

def generate_chart(data):
    """
    Generate a chart based on the provided data and save it as a PNG file.
    data = {"labels": [...], "values": [...]}
    """
    labels = data.get("labels", [])
    values = data.get("values", [])

    plt.figure(figsize=(8, 6))
    plt.bar(labels, values, color=['#ff6384', '#36a2eb', '#cc65fe'])
    plt.xlabel("Options")
    plt.ylabel("Responses")
    plt.title("Questionnaire Results")
    
    # Save chart to a temporary file
    chart_path = f"temp/{uuid.uuid4()}.png"
    os.makedirs("temp", exist_ok=True)
    plt.savefig(chart_path)
    plt.close()
    return chart_path
