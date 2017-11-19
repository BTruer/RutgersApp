function showDiv(elem){
    if(elem.value == 'bc'){
    	document.getElementById('table_bc').style.display = "block";
    	document.getElementById('table_bdh').style.display = "none";
    	document.getElementById('table_ldc').style.display = "none";
  		document.getElementById('table_ndh').style.display = "none";

    }
  	else if (elem.value == 'bdh'){
  		document.getElementById('table_bc').style.display = "none";
    	document.getElementById('table_bdh').style.display = "block";
    	document.getElementById('table_ldc').style.display = "none";
  		document.getElementById('table_ndh').style.display = "none";
  	}
  	else if (elem.value == 'ldc'){
		document.getElementById('table_bc').style.display = "none";
    	document.getElementById('table_bdh').style.display = "none";
    	document.getElementById('table_ldc').style.display = "block";
  		document.getElementById('table_ndh').style.display = "none";
  	}
  	else if (elem.value == 'ndh'){
		document.getElementById('table_bc').style.display = "none";
    	document.getElementById('table_bdh').style.display = "none";
    	document.getElementById('table_ldc').style.display = "none";
  		document.getElementById('table_ndh').style.display = "block";
  	}
}