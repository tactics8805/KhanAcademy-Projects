draw =  function(){
    background (255, 255, 255);
    fill(255, 0, 0);
    textSize(30);
    text("Cursor Tracker", 10, 30);
    fill(252, 65, 65);
    ellipse(210, 30, 9, 9);
    ellipse(220, 30, 9, 9);
    ellipse(230, 30, 9, 9);
    textSize(20);
    fill(255, 0, 0);
    text("Watch the textbox change to the live", 10, 60);
    text("coordinates of your mouse!", 10, 80);
    fill(255, 0, 0);
    var label = mouseX + " , " + mouseY;
    text(label, mouseX, mouseY);
};
