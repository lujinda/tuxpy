String.format = function(src){
    if (arguments.length == 0)
        return null;
    var args = Array.prototype.slice.call(arguments, 1);
    return src.replace(/\{(\d+)\}/g, function(m, i){
        return args[i];
    });
};
function checkbox_checked(name){
    checkboxs = document.getElementsByName(name);
    var checkdCount = 0;
    for (var i = 0; i < checkboxs.length; i++){
        if (checkboxs[i].checked == true){
            checkdCount += 1;
        }
    }
    return checkdCount;
}
function show(event, obj,id) {
    event.preventDefault();
    var objDiv = $("#"+id+"");
    $(objDiv).html(String.format("<li><span>名称/别名:</span> <input name='value' value='{0}'/></li><li><a href='#' OnClick=\"javascript:hide(event, this, 'sort_msg');\">[关闭]</a><a  href=\"javascript:document.sort_msg_form.action='/tuxpy/listsort.py?set_{1}={2}';document.sort_msg_form.submit();\">[保存]</a></li>", obj.innerHTML, obj.name, obj.id));
    $(objDiv).css("display","block");
    $(objDiv).css("left", event.clientX);
    $(objDiv).css("top", event.clientY + 30);
}
function hide(event, obj,id) {
    event.preventDefault();
    var objDiv = $("#"+id+"");
    $(objDiv).css("display", "none");
}
function filterPage(event, target_id){
    event.preventDefault();
    var page_filter = document.getElementsByName('page_filter_title');
    for (i = 0;i < page_filter.length; i = i + 1 ){
        if (page_filter[i].id == target_id){
            page_filter[i].setAttribute("style", "display:block");
        }else{
            page_filter[i].setAttribute("style", "display:none");
        }
    }

}

function doBlog(opera){
    if (! checkbox_checked('blog_checkbox')){
        alert("你还没有选中项");
        return;
    }
    
    if (opera == 'del' && !confirm('你确定要删除所选项')){
        return;
    }
    document.page_msg_form.action="?" + opera + '=1';
    document.page_msg_form.submit();
}
function confirmDel(mess, event){
    if (!confirm(mess)){
        event.preventDefault();
        return ;
    }
}
function move_blog(obj){
    if (! checkbox_checked('blog_checkbox')){
        alert("你还没有选中项");
        return;
    }
    var sort_uuid = obj.value;
    if (sort_uuid == '-1')return;
    document.page_msg_form.action="?move=1";
    document.page_msg_form.submit();
}
function checkAll(s){
    var checkbox_list = document.getElementsByName('blog_checkbox');
    var len = checkbox_list.length;
    for (i=0; i<len; i++)
    {
        checkbox_list[i].checked = s;
    }
}

function will(event){
    alert("不好意思,由于时间赶,该功能还没实现");
    event.preventDefault();
}
$(document).ready(function(){
    function show_tux_summary(summary){
        $("#tux_summary").html(summary).fadeIn();
    };
    $("#goToTop").hide();
    $(function(){
        $(window).scroll(function(){
            if ($(this).scrollTop() > $(window).height() / 3){
                $("#goToTop").fadeIn(1000);
                $("#tux img").fadeOut(800);
            }else{
                $("#goToTop").fadeOut(1000);
                $("#tux img").fadeIn(800);
            }
        });
    });

    $('#goToTop a').click(function (event){
        $('html,body').animate({scrollTop:0}, 'slow');
    });
    $('.sider_content a').mouseenter(function (){
        summary = $(this).next().html();
        if ($(this).next().text().trim())
            show_tux_summary(summary);
    });
    $('.sider_content a').mouseleave(function (){
        $("#tux_summary").hide();
    }); // 鼠标移开后，去掉右上角的提示
    $("#tux_summary").click(function (){
        $(this).fadeOut(1000);
    }).mouseover(function (){
        $(this).fadeOut(1000);
    });
});

