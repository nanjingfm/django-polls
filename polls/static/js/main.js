/**
 * Created by Java on 2017/2/20.
 */

$(function () {
    // top 5 polls
    if ($('#top5polls').length) {
        $.ajax({
            type: 'GET',
            url: topfivepolls,
            beforeSend: function () {
                $('#top5polls').showLoading();
            },
            success: function (result) {
                $('#top5polls').hideLoading();
                $('#top5polls').append(result);
            }
        });
    }
})
