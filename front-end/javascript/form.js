function checkBoxClick()
{
    if(document.getElementById('questions_checkbox').checked)
    {
        document.getElementById('guest-info').style.display = 'block';
        document.getElementById('questions_asked').style.display = 'block';
        document.getElementById('guest-name-div').style.display = 'block';
        document.getElementById('guest-email-div').style.display = 'block';
        document.getElementById('guest-social-media-div').style.display = 'block';
    }
    else
    {        
        document.getElementById('questions_asked').style.display = 'none';
            document.getElementById('guest-info').style.display = 'block';
            document.getElementById('guest-name-div').style.display = 'block';
            document.getElementById('guest-email-div').style.display = 'none';
            document.getElementById('guest-social-media-div').style.display = 'none';
    }
}

function formSubmit()
{
    var complete = true;
    if(!anyRadioBtnSelected('speaker-ratings'))
    {
        complete = false;
    }
    else if(!anyRadioBtnSelected('content-ratings'))
    {
        complete = false;
    }
    else if(document.getElementById('talk-comment').value == "")
    {
        complete =  false;
    }


    if(document.getElementById('questions_checkbox').checked)
    {
        if(document.getElementById('questions').value == "")
        {
            complete = false;
        }
        else if(document.getElementById('guest-name').value == "")
        {
            complete = false;
        }
        else if((document.getElementById('guest-email').value == "") && (document.getElementById('guest-social-media').value == ""))
        {
            complete = false;
        }
    }

    if(document.getElementById('drawing_checkbox').checked)
    {
        if(document.getElementById('guest-name').value == "")
        {
            complete = false;
        }
    }

    if(!complete)
    {
        window.alert('Please make sure all the required fields are filled out.');
    }


    return complete;
}

function anyRadioBtnSelected(radioBtnName)
{
    var btns = document.getElementsByName(radioBtnName);
    for(var i = 0; i < btns.length; i++)
    {
        if(btns[i].type == 'radio' && btns[i].checked)
        {
            return true;
        }
    }

    return false;
}