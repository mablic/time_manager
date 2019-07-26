// define

let interval = {};
let status = {};
let watch = {};
//stop_watch function
function stop_watch(clickID){

	watch[clickID]++;
	totalH = watch[clickID];
	hours = parseInt(totalH / 3600);
	minutes = parseInt((totalH - hours * 3600) / 60);
	seconds = parseInt(totalH - hours * 3600 - minutes * 60);
	if(seconds/60 == 1){
		seconds = 0;
		minutes++;
		if(minutes / 60 == 1){
			minutes = 0;
			hours++;
		}
	}

	if(seconds < 10){
		seconds = "0" + seconds.toString();
	}else{
		seconds = seconds.toString();
	}

	if(minutes < 10){
		minutes = "0" + minutes.toString();
	}else{
		minutes = minutes.toString();
	}

	if(hours < 10){
		hours = "0" + hours.toString();
	}else{
		hours = hours.toString();
	}
	if (document.getElementById("item_display_" + clickID) != null){
		document.getElementById("item_display_" + clickID).innerHTML = hours + ":" + minutes + ":" + seconds;
	}
}

function item_start_stop_(clickID) {
	if(!(clickID in watch)){
		watch[clickID] = 0;
	}
	//start
	if (!(clickID in interval) || status[clickID] == "Stop"){
		interval[clickID]=window.setInterval(function() { stop_watch(clickID) }, 1000);
		document.getElementById("item_start_stop_" + clickID).innerHTML = "Stop";
		status[clickID] = "Start";	
	}else{
	//stop
		window.clearInterval(interval[clickID]);
		document.getElementById("item_start_stop_" + clickID).innerHTML = "Start";
		status[clickID] = "Stop";
	}
}

function item_reset_(clickID){
	window.clearInterval(interval[clickID]);
	watch[clickID] = 0;
	document.getElementById("item_display_" + clickID).innerHTML = "00:00:00";
	document.getElementById("item_start_stop_" + clickID).innerHTML = "Start";
}


function delete_project(){
    console.log("test");
};

function change_background(columnID, colorCode){ //change the backgroup color of a column
	var currColumn = $('#' + columnID);
	var backgroundColor = currColumn.css('background');
	
	if (backgroundColor.indexOf('rgba(0, 0, 0, 0)') == -1 ||
		backgroundColor.indexOf('linear-gradient') != -1){ // background exists already
		var index = backgroundColor.indexOf('none');
		if (index == -1){	// gradient background exists
			var s = backgroundColor.indexOf('(rgb');
			var e = backgroundColor.indexOf('repeat');
			var currColor = backgroundColor.substring(s, e-2);
			currColor += ", " + colorCode + ")"
		}else{ // setup gradient background
			backgroundColor = backgroundColor.substring(0, index-1);
			var currColor = '(' + backgroundColor + ', ' + colorCode + ')';
		}
		currColumn.css('background', 'linear-gradient' + currColor);
	}else{
		currColumn.css('background', colorCode);
	}
}

function remove_background(columnID, indexCol){
	var currColumn = $('#' + columnID);
	var backgroundColor = currColumn.css('background');
	if (backgroundColor.indexOf('rgba(0, 0, 0, 0)') == -1 ||
		backgroundColor.indexOf('linear-gradient') != -1){ // background exists already
		var index = backgroundColor.indexOf('none');
		var s = backgroundColor.indexOf('(rgb');
		if (index == -1){	// gradient background exists
			var colorCodeArray = new Array;
			var e = 0;
			var tmp = '';
			for (i=s; i<backgroundColor.length; i++){
				if (backgroundColor[i] == 'r'){
					s = i;
				}
				else if (backgroundColor[i] == ')' 
					&& i >0 && backgroundColor[i-1] != ')'){
					tmp = backgroundColor.substring(s, i + 1);
					colorCodeArray.push(tmp);
				}
			}
			colorCodeArray.splice(indexCol, 1);
			var colorCode = colorCodeArray.join();
			if (colorCodeArray.length <= 1){
				currColumn.css('background', colorCode);
			}else{
				currColumn.css('background', 'linear-gradient(' + colorCode + ')');
			}
		}else{ // setup gradient background
			currColumn.css('background', '');
		}
	}

}

function date_delete_picker(current){
    // console.log(current);
    $(current).datepicker({
        format: "mm/dd/yyyy",
        showWeek: true,
        firstDay: 1,
        todayHighlight: true,
    });
};