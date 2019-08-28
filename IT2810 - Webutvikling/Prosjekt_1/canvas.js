var canvas = document.querySelector('canvas');

canvas.width = 300;
canvas.height = 300;

var c = canvas.getContext('2d');
var gridWidth = 3;
var gridHeight = 3;
var tileWidth = canvas.width / gridWidth;
var tileHeight = canvas.height / gridHeight;
var colors = ["AliceBlue","AntiqueWhite","Aqua","Aquamarine","Azure","Beige","Bisque","Black","BlanchedAlmond","Blue","BlueViolet","Brown","BurlyWood","CadetBlue","Chartreuse","Chocolate","Coral","CornflowerBlue","Cornsilk","Crimson","Cyan","DarkBlue","DarkCyan","DarkGoldenRod","DarkGray","DarkGrey","DarkGreen","DarkKhaki","DarkMagenta","DarkOliveGreen","DarkOrange","DarkOrchid","DarkRed","DarkSalmon","DarkSeaGreen","DarkSlateBlue","DarkSlateGray","DarkSlateGrey","DarkTurquoise","DarkViolet","DeepPink","DeepSkyBlue","DimGray","DimGrey","DodgerBlue","FireBrick","FloralWhite","ForestGreen","Fuchsia","Gainsboro","GhostWhite","Gold","GoldenRod","Gray","Grey","Green","GreenYellow","HoneyDew","HotPink","IndianRed","Indigo","Ivory","Khaki","Lavender","LavenderBlush","LawnGreen","LemonChiffon","LightBlue","LightCoral","LightCyan","LightGoldenRodYellow","LightGray","LightGrey","LightGreen","LightPink","LightSalmon","LightSeaGreen","LightSkyBlue","LightSlateGray","LightSlateGrey","LightSteelBlue","LightYellow","Lime","LimeGreen","Linen","Magenta","Maroon","MediumAquaMarine","MediumBlue","MediumOrchid","MediumPurple","MediumSeaGreen","MediumSlateBlue","MediumSpringGreen","MediumTurquoise","MediumVioletRed","MidnightBlue","MintCream","MistyRose","Moccasin","NavajoWhite","Navy","OldLace","Olive","OliveDrab","Orange","OrangeRed","Orchid","PaleGoldenRod","PaleGreen","PaleTurquoise","PaleVioletRed","PapayaWhip","PeachPuff","Peru","Pink","Plum","PowderBlue","Purple","RebeccaPurple","Red","RosyBrown","RoyalBlue","SaddleBrown","Salmon","SandyBrown","SeaGreen","SeaShell","Sienna","Silver","SkyBlue","SlateBlue","SlateGray","SlateGrey","Snow","SpringGreen","SteelBlue","Tan","Teal","Thistle","Tomato","Turquoise","Violet","Wheat","White","WhiteSmoke","Yellow","YellowGreen"];

function drawTiles(){
    for (x = 0; x <= gridWidth; x++) {
        for (var y = 0; y <= gridHeight; y++) {
            var id = '#'+y+x;
            console.log(id);
            color = colors[Math.floor((Math.random()) * colors.length)];
            $(id).attr('fill', color);
            c.fillStyle = color;
            c.fillRect(tileWidth*x,tileHeight*y,tileWidth,tileHeight);
            c.lineWidth = 6;
            c.strokeRect(tileWidth*x,tileHeight*y,tileWidth,tileHeight);
        }
    }
}


//drawCircle();
drawTiles();
test();


function drawCircle() {
    var radius = canvas.height / 2
    c.translate(radius, radius);
    radius = radius * 0.8;
    c.arc(0,0, radius, 0, 2*Math.PI);
    c.fillStyle = 'white';
    c.lineWidth = 20;
    c.stroke();
    c.fill();
}

function test(){
    $("#test").attr('fill','red');
}
