{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "source": [
        "from flask import Flask, jsonify\n",
        "import json\n",
        "\n",
        "app = Flask(__name__)\n",
        "\n",
        "@app.route(\"/\")\n",
        "def home():\n",
        "    return \"✅ News Sentiment Classifier is Live!\"\n",
        "\n",
        "@app.route(\"/news\", methods=[\"GET\"])\n",
        "def get_articles():\n",
        "    try:\n",
        "        with open(\"articles_json.json\", \"r\", encoding=\"utf-8\") as f:\n",
        "            data = json.load(f)\n",
        "        return jsonify(data)\n",
        "    except Exception as e:\n",
        "        return jsonify({\"error\": str(e)})\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "    app.run(host=\"0.0.0.0\", port=5000)\n"
      ],
      "metadata": {
        "id": "3QDHtIMl8bNV"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}