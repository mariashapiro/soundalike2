# Soundalike

Final project for Spring 2022 CS 4675 (Advance Internet Computing) taught by Dr. Ling Liu. We use user listening histories from the Million Song Dataset Challenge to make a song recommedation system using collaborative filtering. The workshop and final presentations are included for convenience. 

## Run Instructions

1.	Activate the virtual environment
  * Unix: `./venv/bin/activate`
  * Windows (on Git Bash terminal): `./venv/Scripts/activate.bat`
2.  Install dependencies `npm install`
3.	In a terminal type `npm run start`
4.	In another terminal type `python -m flask run` to start the server

## Python Dependencies
Install with pip (tested with Python 3.9):
- flask (flask_restful, flask_cors)
- numpy
- pandas
- scipy
- implicit

## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode. Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes. You may also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode. See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.

It correctly bundles React in production mode and optimizes the build for the best performance. The build is minified and the filenames include the hashes.

# If you cite us, please mention:
- this github url
- our names: Robert Morgan, Maria Shapiro, and Ajay Vijayakumar
- our class: Georgia Tech CS 4675: Advance Internet Computing
