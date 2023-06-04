# ENG-AI

ENG-AI is an open-source Python application that uses the OpenAI API to enhance images based on a given prompt.

# Installation

## Clone the repository:
git clone https://github.com/<your-github-username>/eng-ai.git

## Create a virtual environment and activate it:
python3 -m venv venv
source venv/bin/activate

## Install the dependencies:
pip install -r requirements.txt

## Set your OpenAI API key:
export OPENAI_API_KEY=your-api-key

## Usage
## To use the application, call the enhance_drawing function with the paths to the input and output images, and the prompt:

from app import enhance_drawing

enhance_drawing('input.png', 'output.png', 'Change the design to improve efficiency and usability')

## License
This project is licensed under the terms of the MIT license.
