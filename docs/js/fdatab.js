function writeDatabase() {

	var name = document.getElementById("name").value;
	var regn = document.getElementById("regn").value;
	var branch = document.getElementById("branch").value;
	var sem = document.getElementById("sem").value;
	var interest = document.getElementById("interest").value;
	var mobile = document.getElementById("mobile").value;
	var email = document.getElementById("email").value;
	// if (name != 0 && branch !=0 && sem !=0 && mobile !=0 && email !=0) {
		if(regn.length!=0 )	{
		  writeUserData(name,regn,email,branch,sem,interest,mobile);

				document.getElementById( 'aftsc' ).style.display = 'none';
				document.getElementById( 'success' ).style.display = 'block';
		}
		else{
			alert("Enter Regd. No. ");
		}

	// }
	// else {
	// 	alert("Please fill all the field");
	// }


}
function writeUserData(name, regn, email, branch, sem, interest, mobile) {

	db.ref('users/' + regn).set({
		Name: name,
		Branch: branch,
		Sem: sem,
		Interest: interest,
		Mobile: mobile,
		Email: email,

	});


}
