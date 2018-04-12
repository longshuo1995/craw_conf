$(function () {
    // 初始化seed
    parent_seed = {
        "url_list": [base_url],
        "result_type": "static_url",
        "model": {}
    }

    temp_parent = parent_seed

    $base_url = $('#base_url')
    $btn_check = $('#btn_check')
    $request_url = $('#request_url')
    $field_name = $('#field_name')
    $field_rule = $('#field_rule')
    $rule_items = $('#rule_items')
    $btn_delete = $('#btn_delete')
    $btn_clear = $('#btn_clear')
    $check_show = $('#check_show')
    // next_list = []
    // position = []

    levels = [$('#level1'), $('#level2'), $('#level3'), $('#level4')]
    current_level = 0


    function clear_UI() {
        $check_show.html('')
        $field_name.val('')
        $field_rule.val('')
    }

    $request_url.change(function () {
        // 更改测试时发送的url：request_url
        request_url = $request_url.val()

        // 确定点击的url所处index
        // h = $request_url.children()
        // $.each(h, function (k ,v) {
        //     if(request_url == v.innerText){
        //         position[position.length-1] = k
        //         set_level(current_level, k)
        //         return
        //     }
        // })
    })

    function show_UI() {
        alert('yy')
    }

    function update_rule_list() {
        // 同步dict 和 左侧的列表展示。
        $rule_items.html('')
        if(temp_parent['model']){
            $.each(temp_parent['model'], function (k, v) {
                if(k != 'url_list' & k != 'model' & k != 'result_type'){
                    check_box = '<input type="checkbox" name="field_names" value="'+k+'"><span onclick="show_UI()">'+k+'</span><br>'
                    $rule_items.append(check_box)
                }
            })
        }
    }


    $btn_clear.click(function () {
        // update_rule_list()
        clear_UI()
    })


    function set_level(i, j) {
        if(i>current_level+1){
            alert('请先指定前面的')
            set_level(i-1, 0)
            return
        }
        clear_UI()

        current_level = i
        // 界面上的展示效果(checkbox的点击)
        for(var index=0; index<levels.length; index++){
            levels[i].prop('checked', false)
        }
        levels[current_level].prop('checked', true)

        temp_parent = parent_seed
        // if(current_level==0){
        //     $request_url.html('')
        //     $request_url.append("<option value='"+base_url+"'>"+base_url+"</option>");
        //     update_rule_list()
        //     return
        // }else{
        //     position = position.slice(0, i-1)
        //     position.push(j)
        // }
        for(var index=0; index<i; index++){
            // temp_parent = temp_map['son_modes'][position[i]]
            temp_parent = temp_parent['model']
        }
        // temp_parent = temp_parent
        $request_url.html('')
        $.each(temp_parent['url_list'], function (i, v) {
            $request_url.append("<option value='"+v+"'>"+v+"</option>");
        })
        // $request_url.val(temp_parent['url_list'][position[position.length-1]])

        // temp_parent = temp_map['son_modes'][position[position.length-1]]
        update_rule_list()
    }


    $request_url.blur(function () {
        request_url = $request_url.val()
        // if(request_url == base_url){
        //     temp_parent = field_maps
        // }else{
        //     index = temp_parent['url_list'].indexOf(request_url)
        // }
    })


    // 给level 设置点击事件
    for(var i=0; i<levels.length; i++){
        temp = i
        levels[i].click(function () {
            i = this
            switch(i.id)
            {
                case "level1":
                    set_level(0, 0)
                    break;
                case "level2":
                    set_level(1, 0)
                    break;
                case "level3":
                    set_level(2, 0)
                    break;
                case "level4":
                    set_level(3, 0)
                    break;
            }
        })
    }


    function next_level() {
        current_level+=1
        current_level=current_level%levels.length
        set_level(current_level)
    }


    $btn_delete.click(function () {
        show_UI()

        // a = [0, 1, 2, 3]
        // b = a.slice(0, 0)
        // alert(b)

        // for(var i=0; i<[].length; i++){
        //     alert('hah')
        // }
        // alert('heh')

        // a ={"dic": ""}
        // d = {"cc": 'heh'}
        // g = a.items() + b.items()
        // console.log(g)
        // a = [1, 2, 3]
        // b = [2, 5, 6]
        // c = a.concat(b)
        // alert(a)
        // l = {"name": "zhangsan"}
        // if(l["lisi"]){
        //     alert("yes")
        // }else{
        //     alert("no")
        // }
    })


    // base_url 文本框更改时的变动
    $base_url.blur(function () {
        base_url = $base_url.val()
        // if(position.length == 0){
        //     parent_seed['url_list'] = [base_url]
        // }
        parent_seed['url_list'] = [base_url]
        $request_url.empty()
        $request_url.append("<option value='"+base_url+"'>"+base_url+"</option>");
    })

    // $request_url.empty()
    // for(var i=0; i<temp_parent['url_list'].length; i++){
    //     $request_url.append("<option value='"+temp_parent['url_list'][i]+"'>"+temp_map['url_list'][i]+"</option>");
    // }

    $('#btn_insert').click(function () {
        db_name = $('#data_name').val()
        table_name = $('#table_name').val()
        source_spider = $('#source_spider').val()
        time_interval = parseInt(eval($('#time_interval').val()))
        is_structing = parseInt($('#is_structing').val())
        $.post('/insert',{'data':JSON.stringify({
                "seed": parent_seed,
                "db_name": db_name,
                "table_name": table_name,
                "source_spider": source_spider,
                "time_interval": time_interval,
                "is_structing": is_structing,
                "base_url": base_url
            })
        },
        function (data) {
            alert(data)
        })
    })
    $btn_check.click(function () {
        $check_show.html('')
        base_url = $base_url.val()
        function merge_list(l) {
            l_merge = ''
            for(var i = 0; i < l.length; i ++){
                l_merge = l_merge +'<br> &nbsp;&nbsp;'+ l[i]
            }
            return l_merge
        }
        data_url = $request_url.val()
        $.post('/check', {'data': JSON.stringify({'base_url': base_url, 'url': data_url, 'temp_parent': temp_parent})}, function (data) {
            result = data.data
            result_values = ''
            temp_parent['model']['url_list'] = []
            for(var i=0; i<result.length; i++){
                field_name = result[i]['field_name']
                result_type = result[i]['result_type']
                result_data = result[i]['result']
                //界面展示
                str_result_data = merge_list(result_data)
                // $check_show.innerHTML = $check_show.innerHTML + str_result_data
                $check_show.append('<br>'+ field_name+':'+str_result_data)
                temp_parent['result_type'] = result_type
                if(temp_parent['result_type'] != 'end'){
                    if(!temp_parent['model']['url_list']){

                        temp_parent['model']['model'] = {}
                    }
                    temp_parent['model']['url_list'] = temp_parent['model']['url_list'].concat(result_data)
                    // for(var j=0; j<=result_data.length; j++){
                    //     temp_parent['son_modes'].push({})
                    // }
                //    select的界面处理
                }
            }
        })
    })
    $('#btn_save').click(function () {
        // 获取字段数据
        if(!temp_parent["model"]){
            temp_parent["model"] = {}
        }
        field_name = $('#field_name').val()
        field_rule = $('#field_rule').val()
        rule_type_value = $('#rule_type').val()
        field_type_value = $('#field_type').val()
        source_type = $('#source_type').val()
        replace_row = $('#replace_row').val()
        replace_result = $('#replace_result').val()
        // temp_parent["mode_data"]['field_name'] = field_name
        // temp_parent["mode_data"]['rule_type'] = rule_type_value
        // temp_parent["mode_data"]['field_type'] = field_type_value
        // temp_parent["mode_data"]['source_type'] = source_type
        // temp_parent["mode_data"]['field_rule'] = field_rule
        // temp_parent["mode_data"]['replace'] = [replace_row, replace_result]
        temp_parent["model"][field_name] =
            {
                'field_name': field_name,
                'rule_type': rule_type_value,
                'field_type': field_type_value,
                'source_type': source_type,
                'field_rule': field_rule,
                'replace':[replace_row, replace_result]
            }
        update_rule_list()
    })
})

