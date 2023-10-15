function updateTime(){
    var now = new Date;
    var hr = now.getHours;
    var min = now.getMinutes;
    var sec = now.getSeconds;
    var ts = hr+':'+min+':'+sec
    document.getElementById('clock').innerHTML = ts;
}