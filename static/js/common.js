function show(event, obj,id) {
    event.preventDefault();
    var objDiv = $("#"+id+"");
    $(objDiv).html("<li><span>名称/别名:</span> <input name='value' value='"+ obj.innerHTML + "'/></li><li><a href='#' OnClick=\"javascript:hide(event, this, 'sort_msg');\">[关闭]</a><a  href=\"javascript:document.sort_msg_form.action='/tuxpy/listsort.py?set_" + obj.name + "=" + obj.id  + "';document.sort_msg_form.submit();\">[保存]</a></li>");
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
