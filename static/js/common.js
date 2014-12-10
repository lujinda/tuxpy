function show(obj,id) {                                                  
    var objDiv = $("#"+id+"");
    $(objDiv).html("<li><span>名称/别名:</span> <input name='value' value='"+ obj.innerHTML + "'/></li><li><a OnClick=\"javascript:hide(this, 'sort_msg');\">[关闭]</a><a  href=\"javascript:document.sort_msg_form.action='/tuxpy/listsort.py?set_" + obj.name + "=" + obj.id  + "';document.sort_msg_form.submit();\">[保存]</a></li>");
    $(objDiv).css("display","block");
    $(objDiv).css("left", event.clientX);
    $(objDiv).css("top", event.clientY + 30);
}
function hide(obj,id) {
    var objDiv = $("#"+id+"");
    $(objDiv).css("display", "none");
}
