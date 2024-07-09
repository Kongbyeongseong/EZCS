function sendResetRequest() {
    let username = $("#forgotPasswordUsername").val();
    let birthdate = $("#birthdate").val();
    let phone_number = $("#phone_number").val();
    let csrf = $("#csrf").val();
    let url = $("#searchPWForm").data("url");

    $.ajax({
        url: url,
        type: "post",
        data: {
            username: username,
            birthdate: birthdate,
            phone_number: phone_number,
            csrfmiddlewaretoken: csrf
        },
        dataType: "json",
        success: function (data) {
            if (data.result === "success") {
                alert(data.msg);
                location.href = "/accounts/reset-password/";
            } else {
                alert(data.msg);
            }
        }
    });
}

function chkUserName() {
    let username = $("#forgotPasswordUsername");
    let name = $("#name").val();
    let phone = $("#phone").val();

    if (username.val().trim() == "") {
        $("#usernameError").text("아이디를 입력하세요.");
        $("#usernameError").show();
        username.addClass("is-invalid");
        if (username.hasClass("is-valid")) {
            username.removeClass("is-valid");
        }
        username.focus();
        return;
    }
}