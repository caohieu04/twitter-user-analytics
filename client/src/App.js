import { React } from "react";
import Report from "./Components/Report";
import { createTheme, ThemeProvider, styled } from '@mui/material/styles';
import "./App.css";

const theme = createTheme({
  typography: {
    fontFamily: [
      'Comic Sans MS',
      'Nunito',
      'Roboto',
      '"Helvetica Neue"',
      'Arial',
      'sans-serif'
    ].join(','),
  }
});

function App() {

  return (
    <ThemeProvider theme={theme}>
      <div className="main">
        {/* <h1>Twitter Search</h1> */}
        {/* <div className="search">
        <TextField
          id="outlined-basic"
          onChange={inputHandler}
          variant="outlined"
          fullWidthredf
          label="Search"
        />
      </div> */}
        <Report />
      </div>
    </ThemeProvider>
  );
}

export default App;