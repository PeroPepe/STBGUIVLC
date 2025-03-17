const { app, BrowserWindow } = require("electron");
const path = require("path");

function createWindow() {
    let win = new BrowserWindow({
        width: 1280,
        height: 720,
        fullscreen: true,
        webPreferences: {
            nodeIntegration: true
        }
    });
    win.loadFile("index.html");
}

app.whenReady().then(createWindow);
