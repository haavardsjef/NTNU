var canvas = document.querySelector('canvas');

canvas.width = 500;
canvas.height = 500;

var c = canvas.getContext('2d');
var svg = document.getElementsByTagName('svg')[0]; //Get svg element
var gridWidth = 18;
var gridHeight = 18;
var tileWidth = canvas.width / gridWidth;
var tileHeight = canvas.height / gridHeight;
var colors = ["AliceBlue", "AntiqueWhite", "Aqua", "Aquamarine", "Azure", "Beige", "Bisque", "Black", "BlanchedAlmond", "Blue", "BlueViolet", "Brown", "BurlyWood", "CadetBlue", "Chartreuse", "Chocolate", "Coral", "CornflowerBlue", "Cornsilk", "Crimson", "Cyan", "DarkBlue", "DarkCyan", "DarkGoldenRod", "DarkGray", "DarkGrey", "DarkGreen", "DarkKhaki", "DarkMagenta", "DarkOliveGreen", "DarkOrange", "DarkOrchid", "DarkRed", "DarkSalmon", "DarkSeaGreen", "DarkSlateBlue", "DarkSlateGray", "DarkSlateGrey", "DarkTurquoise", "DarkViolet", "DeepPink", "DeepSkyBlue", "DimGray", "DimGrey", "DodgerBlue", "FireBrick", "FloralWhite", "ForestGreen", "Fuchsia", "Gainsboro", "GhostWhite", "Gold", "GoldenRod", "Gray", "Grey", "Green", "GreenYellow", "HoneyDew", "HotPink", "IndianRed", "Indigo", "Ivory", "Khaki", "Lavender", "LavenderBlush", "LawnGreen", "LemonChiffon", "LightBlue", "LightCoral", "LightCyan", "LightGoldenRodYellow", "LightGray", "LightGrey", "LightGreen", "LightPink", "LightSalmon", "LightSeaGreen", "LightSkyBlue", "LightSlateGray", "LightSlateGrey", "LightSteelBlue", "LightYellow", "Lime", "LimeGreen", "Linen", "Magenta", "Maroon", "MediumAquaMarine", "MediumBlue", "MediumOrchid", "MediumPurple", "MediumSeaGreen", "MediumSlateBlue", "MediumSpringGreen", "MediumTurquoise", "MediumVioletRed", "MidnightBlue", "MintCream", "MistyRose", "Moccasin", "NavajoWhite", "Navy", "OldLace", "Olive", "OliveDrab", "Orange", "OrangeRed", "Orchid", "PaleGoldenRod", "PaleGreen", "PaleTurquoise", "PaleVioletRed", "PapayaWhip", "PeachPuff", "Peru", "Pink", "Plum", "PowderBlue", "Purple", "RebeccaPurple", "Red", "RosyBrown", "RoyalBlue", "SaddleBrown", "Salmon", "SandyBrown", "SeaGreen", "SeaShell", "Sienna", "Silver", "SkyBlue", "SlateBlue", "SlateGray", "SlateGrey", "Snow", "SpringGreen", "SteelBlue", "Tan", "Teal", "Thistle", "Tomato", "Turquoise", "Violet", "Wheat", "White", "WhiteSmoke", "Yellow", "YellowGreen"];


function drawTiles() {
    for (x = 0; x < gridWidth; x++) {
        for (var y = 0; y < gridHeight; y++) {
            color = colors[Math.floor((Math.random()) * colors.length)];
            addSVGTile(x, y, color);
            addCanvasTile(x, y, color);
        }
    }
}

function drawCircles() {
    var center = canvas.height / 2
    var radius = center * 0.8;

    var newElement = document.createElementNS("http://www.w3.org/2000/svg", 'circle');

    newElement.setAttribute("class", "circle");
    newElement.setAttribute("cx", center);
    newElement.setAttribute("cy", center);
    newElement.setAttribute("r", radius);
    newElement.setAttribute("height", tileHeight);
    newElement.style.fill = 'white'; //Set stroke colour
    newElement.style.stroke = 'black';
    newElement.style.strokeWidth = "10px"; //Set stroke width
    svg.appendChild(newElement);

    c.translate(center, center);
    c.arc(0, 0, radius, 0, 2 * Math.PI);
    c.fillStyle = 'white';
    c.lineWidth = 20;
    c.stroke();
    c.fill();
    c.translate(-center, -center);


}


function addSVGTile(x, y, color) {
    var newElement = document.createElementNS("http://www.w3.org/2000/svg", 'rect');
    newElement.setAttribute("class", "tile");
    newElement.setAttribute("x", tileWidth * x);
    newElement.setAttribute("y", tileHeight * y);
    newElement.setAttribute("width", tileWidth);
    newElement.setAttribute("height", tileHeight);
    newElement.style.fill = color; //Set stroke colour
    newElement.style.stroke = 'black';
    newElement.style.strokeWidth = "5px"; //Set stroke width
    svg.appendChild(newElement);
}

function addCanvasTile(x, y, color) {
    c.fillStyle = color;
    c.fillRect(tileWidth * x, tileHeight * y, tileWidth, tileHeight);
    c.lineWidth = 6;
    c.strokeRect(tileWidth * x, tileHeight * y, tileWidth, tileHeight);
}

$(document).ready(function() {
    $(".tile").mouseenter(function() {
        $(this).fadeOut("slow").delay(30000).fadeIn("slow");

    });
    $(".circle").click(function() {
        $(this).fadeOut().delay(10000).fadeIn();

    });

    $("#canvas").click(function() {
        $(this).fadeOut("slow").delay(3000).fadeIn("slow");

    });

    $("#button").click(function() {
        $("#documentation").slideToggle();
    })
});


drawTiles();
drawCircles();
