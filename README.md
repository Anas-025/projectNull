# ProjectNull

![projectNull](https://github.com/Anas-025/projectNull/assets/102301021/3c755237-0eae-4695-9fbf-6fbd10706354)


## Overview

**ProjectNull** is a Django-based text transformation project hosted at [https://project-null.vercel.app/](https://project-null.vercel.app/). This application utilizes an API for transforming input text and provides users with a web interface to interact with various formatting options.

## Features

- **Django Web Application**: The project is built using the Django framework and is accessible through [https://project-null.vercel.app/](https://project-null.vercel.app/).
- **API Integration**: Utilizes the [Project-Null API](https://project-null.vercel.app/app/api/util/v1/public/transform) for text transformations.
- **Formatting Options**:
  1. Uppercase: Transform the input text to uppercase.
  2. Lowercase: Transform the input text to lowercase.
  3. Character Count in Each Word: Retrieve the character count in each word of the input text.

## Usage

1. **Access the Application:**
   Visit [https://project-null.vercel.app/](https://project-null.vercel.app/) to access the ProjectNull web interface.

2. **Enter Text and Select Formatting Option:**
   - Enter the text you want to transform.
   - Select the desired formatting option: Uppercase, Lowercase, or Character Count in Each Word.

3. **Review Output:**
   - The transformed text and detailed information about the transformation will be displayed on the web page.

## API Information

- **API Endpoint**: [https://project-null.vercel.app/app/api/util/v1/public/transform](https://project-null.vercel.app/app/api/util/v1/public/transform)
- **Data Body Format**: `data={'text': string, 'formatting': number}`
- **Formatting Options**:
  - 1: Uppercase
  - 2: Lowercase
  - 3: Character Count in Each Word

