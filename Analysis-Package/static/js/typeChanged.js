document.getElementById('checkControl').addEventListener('change', () => {
    let inputType = document.getElementById('password');
    if(document.getElementById('checkControl').checked  == true){
            if(inputType.type == 'password'){
                inputType.type = 'text';
            }
    }
    else{
        if(inputType.type == 'text'){
            inputType.type = 'password';
        }
    }
});
