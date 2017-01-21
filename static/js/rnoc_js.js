var modelClassDict = {
    "su_co": "SuCo",
    "trang_thai": "TrangThai",
    "nguyen_nhan": "NguyenNhan",
    "thiet_bi": "ThietBi",
    "thao_tac_lien_quan": "ThaoTacLienQuan",
    "doi_tac": "DoiTac",
    "du_an": "DuAn",
    "component_lien_quan": "Component",
    "lenh_lien_quan": 'Lenh',
};
var last_add_item
SLASH_DISTINCTION = '/'
$(document).ready(function() {
    var option_khong_tu_dong_search_tram

    option_khong_tu_dong_search_tram = $('input#id_khong_search_tu_dong_tram').prop('checked')

    $(".search-w input[type=text]").keyup(function(e) {
        if (e.keyCode == 13) {
            form_table_handle(e, 'intended_for_enter_search')
        }
    });


    //.show-form-modal
    $(this).on('click', '#mll-form-table-wrapper span.input-group-addon,#modal-on-mll-tables span.input-group-addon,a.manager-a-form-select-link,select#id_chon_loai_de_quan_ly,.edit-entry-btn-on-table,form#model-manager input[type=submit],.show-modal-form-link,a.show-modal-form-link_allow_edit,a.searchtable_header_sort,.search-botton,.search-manager-botton,input.what_g_choice', form_table_handle)


    function form_table_handle(e, intended_for, abitrary_url, sort_field) {
        console.log("okkkkkkkkkkkkkkkkk first")
        return_sau_cuoi = false
        class_value = $(this).attr("class")
        is_no_show_return_form = false
        //is_both_table = "both form and table"
        is_table = true
        is_form = true
        form_table_template = "normal form template" //'form_on_modal'
        hieu_ung_sau_load_form_va_table = "khong hieu ung"
        if (intended_for) {
            closest_wrapper = $(e.target).closest('div.form-table-wrapper')
        } else {
            closest_wrapper = $(this).closest('div.form-table-wrapper')
        }
        id_closest_wrapper = closest_wrapper.attr('id') // no importaince

        var table_object
        is_get_table_request_get_parameter = false
        //table_name = '' // table_name dung de xac dinh table , sau khi submit form o modal se hien thi o day, trong truong hop force_allow_edit thi table_name attr se bi xoa 
        if (intended_for == 'intended_for_autocomplete') {
            is_table = true
            is_form = true
            closest_wrapper = $('#form-table-of-tram-info')
            id_closest_wrapper = 'form-table-of-tram-info'
            url = abitrary_url
            type = "GET"
            data = {}

            console.log("$('input#id_khong_search_tu_dong').prop('checked')", $('input#id_khong_search_tu_dong').prop('checked'))
            if ($('input#id_khong_search_tu_dong').prop('checked')) {
                url = updateURLParameter(url, 'search_tu_dong_table_mll', 'no')
            } else {
                url = updateURLParameter(url, 'search_tu_dong_table_mll', 'yes')
            }

            if (name_attr_global != 'object') {

                hieu_ung_sau_load_form_va_table = 'active tram-form-toogle-li'
            }
            console.log('sort_field', sort_field)
            if (sort_field == 'SN1' || sort_field == 'SN2') {
                hieu_ung_sau_load_form_va_table = 'active thong-tin-tram toogle'
            } else if (sort_field == '3G') {
                hieu_ung_sau_load_form_va_table = 'active thong-tin-3g toogle'
            } else if (sort_field == '2G') {
                hieu_ung_sau_load_form_va_table = 'active thong-tin-2g toogle'
            } else if (sort_field == '4G') {
                hieu_ung_sau_load_form_va_table = 'active thong-tin-4g toogle'
            }

        } else if (intended_for == 'intended_for_manager_autocomplete') {
            is_both_table = "both form and table"
            is_table = true
            is_form = true
            closest_wrapper = wrapper_attr_global
            url = abitrary_url
            type = "GET"
            data = {}


            //@@@@@@@@@@@@@@@
        } else if (intended_for == 'intended_for_enter_search' || class_value.indexOf('search-botton') > -1) {
            var query;
            //
            if (intended_for == 'intended_for_enter_search') { //NHAN ENTER
                textinput = $(e.target)
                //query = $(e.target).val();
            } else { //KICK BUTTON
                textinput = $(this).closest('.search-w').find('input[type=text]')
            }
            if (textinput.hasClass('inputtext_for_model')) {
                var query;

                //wrapper_attr_global = $(e.target).closest('.form-table-wrapper')
                //query = wrapper_attr_global.find('#text-search-manager-input').val().split('3G_');
                query = textinput.val()
                url = wrapper_attr_global.find('form').attr('action')
                url = updateURLParameter(url, 'query_main_search_by_button', query)

                is_both_table = 'table only'
                type = "GET"
                data = {}



            } else {
                console.log('tu day', e)
                var query;
                query = textinput.val()
                url = "/omckv2/modelmanager/TramForm/new/"
                url = updateURLParameter(url, 'query_main_search_by_button', query)
                is_both_table = 'table only'
                type = "GET"
                data = {}
                hieu_ung_sau_load_form_va_table = 'active tram-table-toogle-li'
                if (id_closest_wrapper = 'form-table-of-tram-info_dang_le_ra') {
                    closest_wrapper = $('#form-table-of-tram-info')
                    id_closest_wrapper = closest_wrapper.attr('id') // no importaince
                }
            }
        } else if (class_value.indexOf('input-group-addon') > -1) {
            dtuong_before_submit = $(this)
            find_glyphicon_calendar = $(this).find('.glyphicon-calendar')
            if (find_glyphicon_calendar.length > 0) {
                return true
            }
            console.log('dtuong_before_submit', dtuong_before_submit.attr('class'))
            href_id = $(this).find('span.glyphicon').attr("href_id")
            near_input = $(this).closest('.input-group').find('input[type=text]')
            near_input_value = near_input.val()
            console.log('near_input_value 1', near_input_value)
            if (typeof href_id === "undefined") {
                console.log('near_input_value 2', near_input_value)
                if (near_input_value == '') {
                    href_id = "new"
                } else {
                    href_id = near_input_value
                    console.log('near_input_value 3', near_input_value)
                }
            }
            name = modelClassDict[near_input.attr("name")] + 'Form'
            url = "/omckv2/modelmanager/" + name + "/" + href_id + "/"
            is_table = false
            if (href_id == 'new') {
                if (name_attr_global == 'thao_tac_lien_quan' || name_attr_global == 'lenh_lien_quan' || name_attr_global == 'component_lien_quan') {
                    input_text_to_Name_field = last_add_item
                } else {
                    input_text_to_Name_field = near_input.val()
                }
                hieu_ung_sau_load_form_va_table = 'input text to Name field'
            }
            form_table_template = 'form_on_modal'
            closest_table_name = closest_wrapper.find('table').attr('name')

            if (closest_table_name && href_id != 'new') {
                $('#modal-on-mll-table').attr('table_name', closest_table_name)
            } else {
                $('#modal-on-mll-table').removeAttr('table_name')
            }

            type = "GET"
            data = {}

        } else if (class_value.indexOf('search-manager-botton') > -1) {

            wrapper_attr_global = $(e.target).closest('.form-table-wrapper')
            query = wrapper_attr_global.find('#text-search-manager-input').val().split('3G_');
            url = wrapper_attr_global.find('form').attr('action')
            url = updateURLParameter(url, 'query_main_search_by_button', query)

            is_both_table = 'table only'
            type = "GET"
            data = {}
        } else if (class_value.indexOf('what_g_choice') > -1) {
            return_sau_cuoi = true
            value = $(this).val()
            $(this).prop("checked", true)
            console.log('what_g_choice*****', value)
            is_table = true
            is_form = false
            closest_wrapper = $('#form-table-of-tram-info')
            id_closest_wrapper = 'form-table-of-tram-info'
            is_get_table_request_get_parameter = true
            console.log('is_get_table_request_get_parameter', is_get_table_request_get_parameter)

            url = "/omckv2/modelmanager/TramForm/new/"

            if (is_get_table_request_get_parameter) {
                console.log('tai sao khogn vao day')
                get_parameter_toggle = ''
                var table_contain_div
                if (table_object) {
                    table_contain_div = table_object
                } else {
                    if (id_closest_wrapper == 'form-table-of-tram-info') {
                        table_contain_div = $('#tram-table')
                        console.log('tau muon cai nay')
                    } else {
                        table_contain_div = closest_wrapper
                    }
                }
                url = update_parameter_from_table_parameter(table_contain_div, url)

            }


            url = updateURLParameter(url, 'what_g_choice', value)
            type = "GET"
            data = {}

        } else if (class_value.indexOf('searchtable_header_sort') > -1) {
            is_table = true
            is_form = false
            is_both_table = 'table only'
            url = $(this).attr('href')
            if (id_closest_wrapper == 'edit-history-wrapper-div') {
                console.log('$(this)', $(this).attr('class'))
                closest_i_want = $(this).closest('div#form-table-of-tram-info')
                console.log('closest_i_want', closest_i_want)
                console.log('0closest_i_want', closest_i_want.attr('id'))
                if (closest_i_want.attr('id') != 'form-table-of-tram-info') {
                    closest_i_want = $(this).closest('div#mll-form-table-wrapper')
                    console.log('2closest_i_want', closest_i_want)
                    if (closest_i_want.attr('id') != 'mll-form-table-wrapper') {
                        return false
                    } else {
                        console.log('3closest_i_want', closest_i_want.attr('id'))
                        url = updateURLParameter(url, 'model_name', 'Mll')
                        tram_id = closest_i_want.find('#id_id').val()
                        console.log('tram_id', tram_id)
                    }
                } else {
                    url = updateURLParameter(url, 'model_name', 'Tram')
                    tram_id = $('#form-table-of-tram-info').find('#id_id').val()
                    console.log('tram_id', tram_id)
                }
                url = updateURLParameter(url, 'edited_object_id', tram_id)
                url = removeParam('tramid', url)
                //url = url.replace(/&?tramid=([^&]$|[^&]*?&)/i, "")
                console.log('###########url new', url)
            }
            type = "GET"
            data = {}
        } else if (class_value.indexOf('edit-entry-btn-on-table') > -1) {
            is_both_table = "form only"
            is_table = false
            is_form = true
            url = closest_wrapper.find('form#model-manager').attr('action')
            entry_id = $(this).attr('id')
            url = url.replace(/\/\w+\/$/g, '/' + entry_id + '/')
            console.log('url', url)

            if (id_closest_wrapper == 'form-table-of-tram-info') {
                hieu_ung_sau_load_form_va_table = 'active tram-form-toogle-li'
            } else {
                hieu_ung_sau_load_form_va_table = "edit-entry"

            }
            type = "GET"
            data = {}


        } else if (class_value.indexOf('manager-form-select') > -1) {
            is_table = true
            is_form = true
            //url = $('#id_chon_loai_de_quan_ly option:selected').val()
            url = $(this).val() //url = new va method = get
            type = "GET"
            data = {}
            hieu_ung_sau_load_form_va_table = "show search box"


        } else if (class_value.indexOf('manager-a-form-select-link') > -1) {
            is_table = true
            is_form = true
            url = $(this).attr('href')
            type = "GET"
            data = {}
            hieu_ung_sau_load_form_va_table = "show search box 2"

        } else if (class_value.indexOf('show-modal-form-link') > -1) {
            is_table = false
            url = $(this).attr("href") ///omckv2/show-modal-form-link/ThietBiForm/1/
            form_table_template = 'form_on_modal'
            table_name = $(this).closest('table').attr('name')
            if (table_name) {
                $('#modal-on-mll-table').attr('table_name', table_name)
            } else {
                $('#modal-on-mll-table').removeAttr('table_name')
            }
            type = "GET"
            data = {}

            if (class_value.indexOf('add-comment') > -1 || class_value.indexOf('Nhan-Tin-UngCuu') > -1) {
                console.log('dfaslkdfjl')
                mll_id = $(this).closest("tr").find('td.id').html()
                url = updateURLParameter(url, 'selected_instance_mll', mll_id)
            } else if (class_value.indexOf('tinh-hinh-mang') > -1) {
                console.log('tinh hinh mang.****')
                yesterday_or_other = $('#bcn-select').val()
                console.log('yesterday_or_other*****', yesterday_or_other)
                url = updateURLParameter(url, 'yesterday_or_other', yesterday_or_other)
                data = $('#option-bcn-form').serialize()
                url = url + '&' + data
                if (yesterday_or_other == 'theotable') {
                    url = update_parameter_from_table_parameter($('#bcmll .table-manager'), url)
                    console.log('vao day di please')
                }
                is_table = true


            } else if (class_value.indexOf('force_allow_edit') > -1) {
                url = updateURLParameter(url, 'force_allow_edit', 'True')
                $('#modal-on-mll-table').removeAttr('table_name')
            } else if (class_value.indexOf('downloadscript') > -1) {
                is_table = true
                tram_id = $(this).closest('form').find('input[name=id]').val()
                console.log('tram_id', tram_id)
                url = updateURLParameter(url, 'tram_id_for_same_ntp', tram_id)
                hieu_ung_sau_load_form_va_table = 'add class overflow for table'
                console.log('!@#$!@#$1')
            }
        } else if (class_value.indexOf('cancel-btn') > -1) { //cancle buton duoc nhan.
            is_table = true
            is_form = true
            url = $(this).closest('form').attr("action").replace(/\/\d+\//g, '/new/')
            type = "GET"
            data = {}

        } else if (class_value.indexOf('loc-btn') > -1) {
            is_table = true
            is_form = true
            url = $(this).closest('form').attr("action") + '?loc=true'
            type = "GET"
            data = $(this).closest('form').serialize()
            if (id_closest_wrapper == 'form-table-of-tram-info') {
                hieu_ung_sau_load_form_va_table = 'active tram-table-toogle-li'
            }




            //Nhan nut submit  

        } else if (class_value.indexOf('submit-btn') > -1) { // ca truong hop add and edit

            url = $(this).closest('form').attr("action")
            if ($(this).val() == 'EDIT' || $(this).val() == 'Update to db') {
                var edit_reason_value = ''
                while (edit_reason_value == '') {
                    edit_reason_value = prompt("please give the reason", "");

                }
                if (edit_reason_value == null) {
                    return false
                }
            }

            if (id_closest_wrapper == "manager-modal") {
                console.log('sdsdsdsdsdsds')
                table_name = $('#modal-on-mll-table').attr('table_name')
                if (table_name) { // mac du add new commnent hay la edit trang_thai, hay thiet bi thi cung phai is_get_table_request_get_parameter = true
                    is_get_table_request_get_parameter = true
                    table_object = $('table[name=' + table_name + ']').closest('div.table-manager')
                    url = updateURLParameter(url, 'table_name', table_name)
                    is_both_table = "both form and table"
                    is_table = true
                    is_form = true
                    if (url.indexOf('CommentForm') > -1 && $(this).val() == 'ADD NEW') {
                        hieu_ung_sau_load_form_va_table = "change style for add command to edit command"
                    }
                } else {
                    console.log('khong co table object, nhugn nut duoc bam van o trong modal')

                    if (class_value.indexOf('edit-ntp') > -1) {
                        is_get_table_request_get_parameter = true
                        is_table = true
                        is_form = true
                        url = removeParam('update_all_same_vlan_sites', url)
                    } else if (class_value.indexOf('update_all_same_vlan_sites') > -1) {
                        url = updateURLParameter(url, 'update_all_same_vlan_sites', 'yes')
                        is_get_table_request_get_parameter = true
                        is_both_table = "both form and table"
                        is_table = true
                        is_form = true

                    } else { // truong hop config ca, hoac la truong hop add new foreinkey

                        is_table = false
                        is_form = true
                        is_get_table_request_get_parameter = false

                        patt = /([^/]*?)Form\/(.*?)\//
                        res = patt.exec(url)
                        form_name = res[1]
                        if (form_name == 'UserProfile') {
                            hieu_ung_sau_load_form_va_table = "update ca truc info"
                        } else if (form_name == 'ThaoTacLienQuan') {
                            //dtuong_before_submit.attr
                            //near_input = dtuong_before_submit.closest('.input-group').find('input[type=text]')
                            near_input = dtuong_before_submit.closest('.input-group').find('input[type=text]')
                            console.log("serach lai", near_input.val())
                            //near_input.trigger('focus')
                            near_input.focus()
                            near_input.autocomplete("search", near_input.val())
                        }

                    }
                }


            } else { // submit trong normal form
                url = $(this).closest('form').attr("action")
                if (id_closest_wrapper == 'profile-loc-ca') {
                    console.log('khong show 2 nut cancel va loc')
                    is_table = false
                    is_form = true
                    khong_show_2_nut_cancel_va_loc = true
                    url = updateURLParameter(url, 'khong_show_2_nut_cancel_va_loc', khong_show_2_nut_cancel_va_loc)

                } else {
                    is_table = true
                    is_form = true

                    if ($(this).val() == 'EDIT') {
                        is_get_table_request_get_parameter = true
                    } else {
                        is_get_table_request_get_parameter = false
                    }
                }
            }

            console.log('is_get_table_request_get_parameter2', is_get_table_request_get_parameter)
            //get context cua table 
            if (is_get_table_request_get_parameter) {
                console.log('tai sao khogn vao day')
                get_parameter_toggle = ''
                var table_contain_div
                if (table_object) {
                    table_contain_div = table_object
                } else {
                    if (id_closest_wrapper == 'form-table-of-tram-info') {
                        table_contain_div = $('#tram-table')
                        console.log('tau muon cai nay')
                    } else {
                        table_contain_div = closest_wrapper
                    }
                }
                url = update_parameter_from_table_parameter(table_contain_div, url)


                if (!table_object) {
                    url = removeParam('table_name', url)
                }
            }
            if (edit_reason_value) {
                url = updateURLParameter(url, 'edit_reason', edit_reason_value)
            }
            console.log('##after add edit_reason', url)
            type = "POST"
            data = $(this).closest('form').serialize()
        } else {
            console.log('not yet handle ')
            return false
        }
        url = updateURLParameter(url, 'form-table-template', form_table_template)
        url = updateURLParameter(url, 'is_form', is_form)
        url = updateURLParameter(url, 'is_table', is_table)
        if (id_closest_wrapper == 'mll-form-table-wrapper' && is_table) {
            loc_cas = $('select[name="loc_ca"]').val()
            if (loc_cas) {
                newpara = loc_cas.join("d4");

            } else {
                newpara = "None"

            }
            url = updateURLParameter(url, 'loc_ca', newpara)
        }

        patt = /Form\/(.*?)\//
        res = patt.exec(url)
        new_or_id = res[1]
        if (is_form && type == "POST") {
            is_update_icon_if_edit_form = true
        } else {
            is_update_icon_if_edit_form = false
        }
        $.ajax({
            type: type,
            url: url,
            data: data, // serializes the form's elements.
            success: function(data) {

                switch (form_table_template) {
                    case "normal form template":
                        if (is_form & !is_no_show_return_form) {
                            formdata = $(data).find('.form-manager_r').html()
                            if (id_closest_wrapper == 'form-table-of-tram-info') {
                                obj = $('#tram-form')
                            } else {
                                obj = closest_wrapper.children('.form-manager')
                            }
                            formdata = update_icon_info_after_load_edit_form(is_update_icon_if_edit_form, formdata)
                            assign_and_fadeoutfadein(obj, formdata)
                        }

                        if (is_table) { //||table_name la truong hop submit modal form chi load lai phai table(gui di yeu cau xu ly form va table, nhung chi muon hien thi table thoi) 
                            tabledata = $(data).find('.table-manager_r').html()
                            if (table_object) {
                                obj = table_object //table_object = table-manager-object
                            } else if (id_closest_wrapper == 'form-table-of-tram-info') {
                                obj = $('#tram-table')
                            } else {
                                obj = closest_wrapper.children('.table-manager')
                            }
                            must_shown_tab_ok = false
                            if (obj.attr('id') == 'tram-table' & hieu_ung_sau_load_form_va_table == 'active tram-table-toogle-li' & $('#tram-table-toogle').attr('class').indexOf('active') == -1) {
                                console.log('i click it...............')
                                //$('#tram-table-toogle-li a').trigger('click')
                                $('.nav-tabs a[href="#tram-table-toogle"]').tab('show')
                                must_shown_tab_ok = true

                            }
                            if (must_shown_tab_ok) {

                                $('#tram-manager-lenh-nav-tab-wrapper-div .nav-tabs a').on('shown.bs.tab', function() {
                                    assign_and_fadeoutfadein(obj, tabledata)
                                    scrolify_fix_table_header(obj.find('table.table-bordered'), 580); // 160 is height 
                                    $('#tram-manager-lenh-nav-tab-wrapper-div .nav-tabs a').unbind('shown.bs.tab');
                                });
                                return false
                            } else {
                                assign_and_fadeoutfadein(obj, tabledata)
                                scrolify_fix_table_header(obj.find('table.table-bordered'), 580); // 160 is height   
                            }
                            if (intended_for == 'intended_for_autocomplete' && !$('input#id_khong_search_tu_dong').prop('checked')) {
                                table2data = $(data).find('.table-manager_r2').html()
                                obj = $('div#mll-form-table-wrapper > div.table-manager')
                                assign_and_fadeoutfadein(obj, table2data)
                                scrolify_fix_table_header(obj.find('table.table-bordered'), 580); // 160 is height    
                            }
                        }
                        break;
                    case 'form_on_modal': // chi xay ra trong truong hop click vao link show-modal
                        {
                            formdata = $(data).find('.wrapper-modal').html()
                            formdata = update_icon_info_after_load_edit_form(is_update_icon_if_edit_form, formdata)
                            $("#modal-on-mll-table").html(formdata)
                            $("#modal-on-mll-table").modal()
                        }
                        break;
                }
                if (hieu_ung_sau_load_form_va_table == 'edit-entry') {
                    var navigationFn = {
                        goToSection: function(id) {
                            $('html, body').animate({
                                scrollTop: $(id).offset().top
                            }, 0);
                        }
                    }
                    navigationFn.goToSection('#' + id_closest_wrapper + ' ' + '.form-manager');
                    return false
                } else if (hieu_ung_sau_load_form_va_table == "hide modal") {
                    $("#modal-on-mll-table").modal("hide")
                } else if (hieu_ung_sau_load_form_va_table == 'add class overflow for table') {
                    console.log('!@#$!@#$2')
                    new_attr = $('#manager-modal').find('.table-manager').attr('class') + ' overflow'
                    $('#manager-modal').find('.table-manager').attr('class', new_attr)
                } else if (hieu_ung_sau_load_form_va_table == "show search box") {
                    $('#manager #search-manager-group').show()
                } else if (hieu_ung_sau_load_form_va_table == "show search box 2") {
                    $('#manager #search-manager-group').show()
                    $("#dropdown-toggle-manager").dropdown("toggle");
                } else if (hieu_ung_sau_load_form_va_table == 'active tram-form-toogle-li') {
                    $('#tram-form-toogle-li a').trigger('click')
                } else if (hieu_ung_sau_load_form_va_table == 'active thong-tin-tram toogle') {
                    $('#tram-form-toogle-li a').trigger('click')
                    $('a[href="#thong-tin-tram"]').trigger('click')
                } else if (hieu_ung_sau_load_form_va_table == 'active thong-tin-3g toogle') {
                    $('#tram-form-toogle-li a').trigger('click')
                    $('a[href="#thong-tin-3g"]').trigger('click')
                } else if (hieu_ung_sau_load_form_va_table == 'active thong-tin-2g toogle') {
                    $('#tram-form-toogle-li a').trigger('click')
                    $('a[href="#thong-tin-2g"]').trigger('click')
                } else if (hieu_ung_sau_load_form_va_table == 'active thong-tin-4g toogle') {
                    $('#tram-form-toogle-li a').trigger('click')
                    $('a[href="#thong-tin-4g"]').trigger('click')
                } else if (hieu_ung_sau_load_form_va_table == "update ca truc info") {
                    ca_moi_chon = closest_wrapper.find('select#id_ca_truc option:selected').html()
                    console.log('@@@@ca_moi_chon', ca_moi_chon)
                    $('span#ca-dang-truc').html('Ca ' + ca_moi_chon)
                } else if (hieu_ung_sau_load_form_va_table == "change style for add command to edit command") {
                    dtuong = $('#modal-on-mll-table h4.add-command-modal-title')
                    dtuong.css("background-color", "#ec971f")
                } else if (hieu_ung_sau_load_form_va_table == 'input text to Name field') {
                    $('div#manager-modal input#id_Name').val(input_text_to_Name_field)
                }
            },
            error: function(request, status, error) {
                
                error = error.toUpperCase()

                console.log('bi loi 400 hoac 403', error,typeof(error))
                if (error == 'FORBIDDEN') { //403
                    console.log(request.responseText)
                    data = $(request.responseText).find('#info_for_alert_box').html()
                    alert(data);
                } else if (error == 'BAD REQUEST') {
                    console.log('bi loi 400')
                    formdata = $(request.responseText).find('.form-manager_r').html()
                    if (id_closest_wrapper == 'form-table-of-tram-info') {
                        console.log("##########1")
                        obj = $('#tram-form')
                    } else {
                        console.log("##########2")
                        obj = closest_wrapper.children('.form-manager')
                    }
                    obj.html(formdata);

                }

            }

        });
        return return_sau_cuoi; //ajax thi phai co cai nay. khong thi , gia su click link thi 
    }
    $(this).on('click', '#submit-id-copy-tin-nhan', function() {
        copyToClipboard(document.getElementById("id_noi_dung_tin_nhan"));
        return false
    })

    $(this).on('click', '#submit-id-copy-bao-cao', function() {
        console.log('dfasdfdsfslkdjflkalklkdfjlkd')
        copyToClipboard(document.getElementById("id_noi_dung_bao_cao"));
        return false
    })


    var obj_autocomplete = {
        create: function() {

            $(this).data('ui-autocomplete')._renderItem = function(ul, item) {
                return $(' <li class="abc" ' + 'thietbi="' + item.label + '">')
                    .append("<a>" + '<b>' + item.label + '</b>' + "<br>" + '<span class="std">' + item.desc + '</span>' + "</a>")
                    .appendTo(ul);
            }
        },
        search: function(e, ui) {
            console.log('dang search')
            showloading = false
            name_attr_global = $(e.target).attr("name")
            wrapper_attr_global = $(e.target).closest('.form-table-wrapper')

        },
        source: function(request, response) {
            query = request.term
            $.get('/omckv2/autocomplete/', {
                query: query,
                name_attr: name_attr_global
            }, function(data) {
                return_data = data['key_for_list_of_item_dict']
                if (query == 'tatca') {
                    number_dau_hieu_co_add = 0
                    is_curent_add = 0
                    response(return_data)
                    return false
                }
                if (name_attr_global == "doi_tac" || name_attr_global == "nguyen_nhan" || name_attr_global == "du_an" || name_attr_global == "su_co" || name_attr_global == "thiet_bi" || name_attr_global == "trang_thai")

                {
                    dtuong = wrapper_attr_global.find('#div_id_' + name_attr_global + ' .glyphicon')
                    if (data['dau_hieu_co_add']) { //if + au new
                        show_only_glyphicon(dtuong, 'glyphicon-log-in')
                        dtuong.attr('href_id', "new")
                    } else {
                        show_only_glyphicon(dtuong, 'glyphicon-info-sign')
                        dtuong.attr('href_id', data['href_id'])
                    }
                } else if (name_attr_global == "thao_tac_lien_quan" || name_attr_global == "lenh_lien_quan" || name_attr_global == "component_lien_quan") {
                    dtuong = wrapper_attr_global.find('#div_id_' + name_attr_global + ' .glyphicon')
                    is_curent_add = data['curent_add']
                    number_dau_hieu_co_add = data['dau_hieu_co_add'] //0,1,2
                    console.log('number_dau_hieu_co_add trong source', number_dau_hieu_co_add)
                    if (number_dau_hieu_co_add) { //co add
                        show_only_glyphicon(dtuong, 'glyphicon-log-in')
                        dtuong.html(number_dau_hieu_co_add)
                        dtuong.attr('href_id', "new")
                        last_add_item = data['last_add_item']
                    } else {
                        show_only_glyphicon(dtuong, 'glyphicon-info-sign')
                        dtuong.attr('href_id', data['href_id'])
                    }
                }

                response(return_data)
            })
        },
        select: function(event, ui) {

            dtuong = wrapper_attr_global.find('#div_id_' + name_attr_global + ' .glyphicon')
            if (name_attr_global == "specific_problem_m2m") {
                this.value = ui.item['label'] + SLASH_DISTINCTION
            } else if (name_attr_global == "doi_tac") {
                if (ui.item['desc'] == "chưa có sdt" || !ui.item['desc']) {
                    this.value = ui.item['label']
                } else {
                    this.value = ui.item['label'] + SLASH_DISTINCTION + ui.item['desc'];
                }
                show_only_glyphicon(dtuong, 'glyphicon-info-sign')
                dtuong.attr("href_id", ui.item['id'])
            } else if (name_attr_global == 'thao_tac_lien_quan' || name_attr_global == 'lenh_lien_quan' || name_attr_global == 'component_lien_quan') {
                var terms = split(this.value);
                // remove the current input
                current_input = terms.pop().replace('\s+', '');
                x = number_dau_hieu_co_add - is_curent_add
                // add the selected item
                terms.push(ui.item['label']);
                // add placeholder to get the comma-and-space at the end
                terms.push("");
                this.value = terms.join(", ");

                //x  chinh la dau hieu co add

                if (x) { //if dau_hieu_co_add
                    show_only_glyphicon(dtuong, 'glyphicon-log-in')
                    dtuong.html(x)
                    dtuong.attr("dau_phon", 'new')
                    dtuong.attr("href_id", 'new')

                } else {
                    console.log("ui.item['id']", ui.item['id'])
                    show_only_glyphicon(dtuong, 'glyphicon-info-sign')
                    dtuong.html('')
                    dtuong.attr("href_id", ui.item['id'])

                }

            } else {
                if (name_attr_global == 'nguyen_nhan' || name_attr_global == 'du_an' || name_attr_global == 'su_co' || name_attr_global == "thiet_bi" || name_attr_global == "trang_thai") {
                    show_only_glyphicon(dtuong, 'glyphicon-info-sign')
                    dtuong.attr("href_id", ui.item['id'])
                }


                this.value = ui.item['label']
            }
            return false
        }

    }

    $(this).on("focus", ".autocomplete", function() {
        if (!$(this).data("autocomplete"))

        {
            $(this).autocomplete(obj_autocomplete)
        }
    });

    $(this).on('click', ".autocomplete,.autocomplete_search_tram,.autocomplete_search_manager", function() {
        value = $(this).val()
        if (value.length === 0) {
            value = 'tatca'
            if ($(this).hasClass('autocomplete')) {

            }
        }
        $(this).autocomplete("search", value)

    });



    $(this).on("keyup", ".autocomplete", function() {
        if ($(this).val().length === 0) {
            closest_wrapper = $(this).closest('div.form-table-wrapper')
            doituong = closest_wrapper.find('#div_id_' + name_attr_global + ' .glyphicon')
            show_only_glyphicon(dtuong, 'glyphicon-plus')
            doituong.removeAttr("href_id")
            if ($(this).attr('name') == 'thao_tac_lien_quan' || $(this).attr('name') == 'lenh_lien_quan' || $(this).attr('name') == 'component_lien_quan') {
                doituong.html('')
            }
        }
    });




    $(this).on("focus", ".autocomplete_search_tram", function() {
        $(this).autocomplete({
            create: function() {
                $(this).data('ui-autocomplete')._renderItem = function(ul, item) {
                    return $('<li class="li-select-in-autocomplete-result">').append(
                            $('<div>').append('<b>' + '<span class="greencolor">' + item.sort_field + ":</span>" + '<span class="">' + item.label + '</span>' + '</b>')
                            .append('<div class="table-type-wrapper">' +
                                '<div  class="wrapper-a-tr"><div class="wrapper-dt-autocomplete" >' + '<span class="tram_field_name">SN1: </span>' + '<span class="chontram" type-tram = "SN1" type-thiet-bi = "2G&3G">' + item.sn1 + '</span>' + '</div>' + '<div class="wrapper-dt-autocomplete" >' + '<span class="tram_field_name">SN2: </span>' + '<span class="chontram" type-tram = "SN2" type-thiet-bi = "2G&3G">' + item.sn2 + '</span>' + '</div></div>' +
                                '<div class="wrapper-a-tr"><div class="wrapper-dt-autocomplete" >' + '<span class="tram_field_name">3G: </span>' + '<span class="chontram" type-tram = "3G" type-thiet-bi = "' + item.s3g_thietbi + '">' + item.s3g + '</span>' + '</div>' + '<div class="wrapper-dt-autocomplete" >' + '<span class="tram_field_name">2G: </span>' + '<span class="chontram" type-tram = "2G" type-thiet-bi  = "' + item.s2g_thietbi + '">' + item.s2g + '</span>' + '</div></div>' +
                                '<div class="wrapper-a-tr"><div class="wrapper-dt-autocomplete" >' + '<span class="tram_field_name">4G: </span>' + '<span class="chontram" type-tram = "4G" type-thiet-bi = "' + item.s4g_thietbi + '">' + item.s4g + '</span>' + '</div>' + '<div class="wrapper-dt-autocomplete" >' + '<span class="tram_field_name">Booster: </span>' + '<span class="chontram" type-tram = "Booster" type-thiet-bi = "' + item.booster_thietbi + '">' + item.booster + '</span>' + '</div>' + '</div>' +
                                '</div>'))
                        .appendTo(ul)
                }
            },
            focus: function(event, ui) {
                event.preventDefault(); // Prevent the default focus behavior.
                return false;
            },
            search: function(e, ui) {
                showloading = false
                name_attr_global = $(e.target).attr("name") //name_attr_global de phan biet cai search o top of page or at mllfilter

            },
            source: function(request, response) {

                console.log('name_attr_global', name_attr_global)
                var query = extractLast(request.term)
                $.get('/omckv2/autocomplete/', {
                    query: query,
                    name_attr: name_attr_global
                }, function(data) {
                    return_data = data['key_for_list_of_item_dict']
                    response(return_data)
                })
            },
            select: function(event, ui) {
                doituongvuaclick = $(event.toElement)
                if (doituongvuaclick.attr('class') == 'chontram') {
                    sort_field = doituongvuaclick.attr('type-tram')
                    console.log('sort_field', sort_field)
                    thiet_bi = doituongvuaclick.attr('type-thiet-bi')
                    value_select = event.toElement.innerText

                } else {
                    sort_field = ui.item.sort_field
                    value_select = ui.item['label']
                    thiet_bi = ui.item.thiet_bi
                }
                /*
                if (name_attr_global == "object") {
                    var terms = split(this.value);
                    // remove the current input
                    terms.pop();
                    // add the selected item
                    terms.push(value_select);
                    // add placeholder to get the comma-and-space at the end
                    terms.push("");
                    this.value = terms.join(", ");
                } else {
                    this.value = value_select; //this.value tuc la gia tri hien thi trong input text
                } */
                var terms = split(this.value);
                // remove the current input
                terms.pop();
                // add the selected item
                terms.push(value_select);
                // add placeholder to get the comma-and-space at the end
                terms.push("");
                this.value = terms.join(", ");



                if (name_attr_global == "object") {
                    $('#id_site_name').val(ui.item.site_name_1)
                    thiet_bi_input_text = $('#mll-form-table-wrapper input#id_thiet_bi')
                    thiet_bi_input_text.val(thiet_bi)
                    dtuong = thiet_bi_input_text.closest('.input-group').find('.glyphicon')
                    show_only_glyphicon(dtuong, 'glyphicon-info-sign')

                    thiet_bis = thiet_bi.split('/')
                    console.log('thiet_bi888', thiet_bi)
                    $('select#id_type_2g_or_3g option:contains("' + thiet_bis[2] + '")').prop('selected', true);
                    $('select#id_brand option:contains("' + thiet_bis[1] + '")').prop('selected', true);
                }
                option_khong_tu_dong_search_tram = $('input#id_khong_search_tu_dong_tram').prop('checked')
                if (!(option_khong_tu_dong_search_tram && name_attr_global == "object")) {
                    form_table_handle(event, 'intended_for_autocomplete', '/omckv2/modelmanager/TramForm/' + ui.item.id + '/?tramid=' + ui.item.id, sort_field)
                }

                return false // return thuoc ve select :
            }

        }) //close autocompltete
    });
    $(this).on("focus", ".autocomplete_search_manager", function(e) {
        $(this).autocomplete({
            create: function() {
                $(this).data('ui-autocomplete')._renderItem = function(ul, item) {
                    return $(' <li class="abc" ' + 'thietbi="' + item.label + '">')
                        .append("<a>" + '<b>' + item.label + '</b>' + "<br>" + '<span class="std">' + item.desc + '</span>' + "</a>")
                        .appendTo(ul);
                }
            },
            focus: function(event, ui) {
                event.preventDefault(); // Prevent the default focus behavior.
                return false;
            },
            search: function(e, ui) {
                name_attr_global = $(e.target).attr("name") //name_attr_global de phan biet cai search o top of page or at mllfilter
                wrapper_attr_global = $(e.target).closest('.form-table-wrapper')
                model_attr_global = wrapper_attr_global.find('form').attr('action')
                patt = /\/(\w*?)Form\//i
                res = patt.exec(model_attr_global)
                console.log('model_attr_global', res[1])
                model_attr_global = res[1]
            },
            source: function(request, response) {
                console.log('name_attr_global', name_attr_global)
                var query = extractLast(request.term)
                $.get('/omckv2/autocomplete/', {
                    query: query,
                    name_attr: name_attr_global,
                    model_attr_global: model_attr_global
                }, function(data) {
                    response(data['key_for_list_of_item_dict'])
                    //response(projects)
                })
            },
            select: function(event, ui) {
                this.value = ui.item['label']
                form_table_handle(event, 'intended_for_manager_autocomplete', '/omckv2/modelmanager/' + model_attr_global + 'Form/' + ui.item.id + '/?tramid=' + ui.item.id)

                return false // return thuoc ve select :
            }

        }) //close autocompltete
    });

    //LENH Chon lenh
    var counter = 0;
    $(this).on('click', 'table.lenh-table > tbody >tr >td.selection>input[type=checkbox] ', function() {
        this_check_box = $(this)
        chosing_row_id = this_check_box.closest("tr").find('td.id').html()
        is_check_state_before_click = this_check_box.is(':checked')
        console.log('is_check', is_check_state_before_click)
        if (false) { /* bo chon 1 row*/
            console.log(chosing_row_id)
            $("table#selected-lenh-table").find("td.id").filter(function() {
                var id = $(this).html();
                if (id == chosing_row_id) {
                    $(this).parent().remove();
                    var index = choosed_command_array_global.indexOf(id);
                    if (index > -1) {
                        choosed_command_array_global.splice(index, 1);
                    }
                    counter = $('#selected-lenh-table tr').length - 1;
                    console.log('ban da bo chon 1 row lenh', choosed_command_array_global)
                }
            }) /* close brace for filter function*/

        } /* close if*/
        else {
            this_check_box.prop("checked", true)
            counter = counter + 1
            var newrowcopy = $('<tr>');
            this_check_box.closest("tr").find('td').each(function(i, v) {
                this_td = $(this)
                if (!this_td.hasClass("selection") && i < 5) { /*khong add nhung selection data*/
                    var this_td_html = $(this).prop('outerHTML') //cu
                    newrowcopy.append(this_td_html)

                }
            });

            command = this_check_box.closest('tr').find('td.command').html()
            var reg = /\[(thamso.*?)\]/g;
            var matches_thamso_attribute_sets = []
            var found
            while (found = reg.exec(command)) {
                console.log('found.index', found.index, 'found', found, '\nreg.lastIndex', reg.lastIndex)
                matches_thamso_attribute_sets.push(found[1]);
                reg.lastIndex = found.index + 1;

            }
            newtd = $('<td>')
            $.each(matches_thamso_attribute_sets, function(index, thamso_name) {
                newtd.append($('<p>').html(thamso_name))
                newtd.append($('<input/>').attr({
                    type: 'text',
                    id: thamso_name
                }))

            })
            if (command.indexOf('[TG]') > -1) {
                newtd.append($('<p>').html('chon TG 1800'))
                newtd.append($('<input/>').attr({
                    type: 'checkbox',
                    class: "chon-TG-1800"
                }))
            }
            newtd.append('<div><input type="button" class="ibtnDel"  value="Delete"><input type="button" class="move up"  value="Up"><input type="button" class="move down"  value="Down"></div></td>')
            newrowcopy.append(newtd);
            $("table#selected-lenh-table>tbody").append(newrowcopy)
            choosed_command_array_global.push(chosing_row_id)
            console.log(choosed_command_array_global)
        }

    });


    // LENH xoa 1 lenh trong table chon lenh
    $("table#selected-lenh-table").on("click", ".ibtnDel", function(event) {
        is_ton_tai_them_1_tr_id = false
        tr_id = $(this).closest("tr").find('td.id').html()
        $(this).closest("tr").remove();

        $("table#selected-lenh-table").find('tbody tr td.id').each(function() {
            if (this.html() == tr_id) {
                is_ton_tai_them_1_tr_id = true
            }

        })
        if (!is_ton_tai_them_1_tr_id) {
            $('table.lenh-table').find('tr td  input[value =' + tr_id + ']').attr('checked', false)
            counter -= 1
        }
    });



    //LENH generate
    $(this).on('click', '.generate-command', function() {
        var command_set_many_tram = "";
        $('.tram-table > tbody > tr').each(function() {
            var command_set_one_tram = "";
            var tram_row = $(this)
            $('#selected-lenh-table > tbody > tr').each(function() {
                tr = $(this)
                var one_command = $(this).find('td.command').html();
                var reg = /\[(.+?)\]/g;
                var matches_tram_attribute_sets = []
                var found
                while (found = reg.exec(one_command)) {
                    matches_tram_attribute_sets.push(found[1]);
                    reg.lastIndex = found.index + 1;
                }
                $.each(matches_tram_attribute_sets, function(index, tram_attribute) {
                    value = tram_row.find('td.' + tram_attribute.split(" ").join("_")).html()
                    console.log('tram_attribute 2', tram_attribute)
                    if (tram_attribute == 'Site ID 3G') {
                        value = value.replace(/^ERI_3G_/g, '')
                    } else if (tram_attribute == 'Site ID 2G') {
                        value = value.replace(/^SRN_2G_/g, '')
                    } else if (tram_attribute.indexOf('thamso') > -1) {
                        value = tr.find('input#' + tram_attribute).val()
                    } else if (tram_attribute == 'TG') {

                        is_check = tr.find('input.chon-TG-1800')
                        is_check = is_check.is(":checked")
                        if (is_check) {
                            value = tram_row.find('td.' + 'TG_1800').html()
                        }
                    }
                    one_command = one_command.replace('[' + tram_attribute + ']', value)
                });
                command_set_one_tram += one_command + '\n\n\n'
            });

            command_set_many_tram += command_set_one_tram + '\n\n'
        });

        $('textarea.command-erea').val(command_set_many_tram);
        console.log(command_set_many_tram)
    });


    $(this).on('click', 'table#selected-lenh-table tbody tr td input.move', function() {
        var row = $(this).closest('tr');
        if ($(this).hasClass('up'))
            row.prev().before(row);
        else
            row.next().after(row);
    });

    $(this).on('click', '.link_to_download_scipt', function() {
        form = $(this).closest('form')
        var data = form.serialize()
        if (form.find('#id_ntpServerIpAddressPrimary').val() == '' || form.find('#id_ntpServerIpAddress1').val() == '') {
            alert('kiem tra lai may cai o trong kia')
            return false
        }
        site_id = $('#form-table-of-tram-info').find('input#id_id').val()
        var win = window.open('/omckv2/download_script_ntp/' + '?site_id=' + site_id + '&' + data);
        if (win) {
            //Browser has allowed it to be opened
            $("#config_ca_modal").modal("hide");
            win.focus();
        } else {
            //Broswer has blocked it
            alert('Please allow popups for this site');
        }
        return false
    })

    $(this).on('click', '.download-bcn', function() {
        console.log('i love you thannk you')
        id = $(this).attr('id')
        //id =='download-bcn'


        data = $('#option-bcn-form').serialize()
        url = $(this).attr('href')
        url = url + '&' + data
        console.log('new url **********', url)
        yesterday_or_other = $('#bcn-select').val()
        url = updateURLParameter(url, 'download-bcn', 'yes')
        //url = updateURLParameter(url, 'yesterday_or_other', yesterday_or_other)
        if (yesterday_or_other == 'theotable') {
            url = update_parameter_from_table_parameter($('#bcmll .table-manager'), url)
        }
        if (id == 'download-keo-dai') {
            url = updateURLParameter(url, 'download-keo-dai', 'yes')
        }

        var win = window.open(url);
        if (win) {
            //Browser has allowed it to be opened
            win.focus();
        } else {
            //Broswer has blocked it
            alert('Please allow popups for this site');
        }
        return false
    })

    $(this).on("click", ".btnEdit", function() {
        var array_td_need_edit = [] //array la chua nhung index cua td can edit
        var par = $(this).parent().parent();
        wrapper_table = $(this).closest('table')
        table_class = wrapper_table.attr("class") //tr
        if (table_class.indexOf('history-table') > -1) {
            array_td_need_edit = [4]
        } else if (table_class.indexOf('doi_tac-table') > -1) {
            array_td_need_edit = [1, 2, 3, 4, 5, 6]
        }
        this_rows = par.children('td')
        var total = this_rows.length;
        this_rows.each(function(i, v) {
            this_html = $(this).text()
            this_html = ((this_html == "—") ? "" : this_html)
            if (array_td_need_edit.indexOf(i) > -1) {
                $(this).html("<input type='text' id='" + $(this).attr("class") + "' value='" + this_html + "'/>");
            } else if (i == total - 1) {
                $(this).html("<img src='media/images/disk.png' class='btnSave'/>");
            }
        })

    });
    $(this).on("click", ".btnSave", function() {
        wrapper_table = $(this).closest('table')
        table_class = wrapper_table.attr("class")
        table_div = $(this).closest('div.table-div')
        url = wrapper_table.attr("table-action")
        table = $(this).closest('.table-manager')
        var trow = $(this).parent().parent(); //tr
        history_search_id = trow.find('td.id').html()
        var row = {
            action: "edit"
        };
        row.history_search_id = history_search_id
        trow.find('input,select,textarea').each(function() {
            row[$(this).attr('id')] = $(this).val();
        });
        if (table_class.indexOf('history-table') > 0) {
            $.get(url, row, function(data) {
                table.html(data)
            });
        } else if (table_class.indexOf('doi_tac-table') > 0) {
            $.get(url, row, function(data) {
                console.log(data);
                $('#table-doitac').html(data);
            });
        }

    });


    $(this).on("click", ".btnDelete", function() {
        wrapper_table = $(this).closest('table')
        table_div = $(this).closest('.table-manager')
        table_class = wrapper_table.attr("class")
        url = wrapper_table.attr("table-action")
        var trow = $(this).parent().parent(); //tr
        history_search_id = trow.find('td.id').html()

        if (table_class.indexOf('history-table')) {
            $("#myModal").find('div#id-deleted-object').html("Doi tuong xoa co id " + history_search_id)
            if (confirm("Are you sure?")) {
                $.get(url, {
                        "action": "delete",
                        "history_search_id": history_search_id
                    },
                    function(data) {
                        table_div.html(data);
                    });
                return false; //url = '/omckv2/edit_history_search/',
            }
        }

    });



    $('.datetimepicker').datetimepicker({
        format: DT_FORMAT,
    });
    $('.datetimepicker_bcn').datetimepicker({
        format: BCN_DT_FORMAT,
    });
    $('.datetimepicker_only_date').datetimepicker({
        viewMode: 'days',
        format: DATE_FORMAT,
    });


    $('.mySelect2').select2({
        width: '100%'
    });
    $('.selectmultiple').select2({
        width: '100%'
    })

    $('#modal-on-mll-table').on('hidden.bs.modal', function(e) {
        // do something...
        $(this).empty()
    })


    $(this).on('click', '#replace-carrier-return', function() {

        value = $('#mll-form-table-wrapper #id_specific_problem_m2m').val().replace('\n', '').replace('\r', '')
        console.log('iloveyuou', value)
        $('#mll-form-table-wrapper #id_specific_problem_m2m').val(value)
    })

    scrolify_fix_table_header($('#mll-table-id'), 580); // 160 is height     
    scrolify_fix_table_header($('#tram-table-id'), 580); // 160 is height     
    $("#loading").hide();
    $('#submit-id-command-cancel').hide()
    $(this).on("ajaxStart", function() {
        if (showloading == true) {
            $("#loading").show();
        }
        showloading = true
    })

    // $(this).on('click', "input[type=submit]", function() {
    //     $("input[type=submit]").removeAttr("clicked");
    //     $(this).attr("clicked", "true");
    // });

    $(this).ajaxComplete(function(event, xhr, settings) {
        $("#loading").hide();
        $('.datetimepicker_bcn').datetimepicker({
            format: BCN_DT_FORMAT
        });

        $('.datetimepicker').datetimepicker({
            format: DT_FORMAT,
        });

        $('.datetimepicker_only_date').datetimepicker({
            viewMode: 'days',
            format: DATE_FORMAT,
        });
        $('.mySelect2').select2({
            width: '100%'
        });
        $('.selectmultiple').select2({
            width: '100%'
        })

    });

}); //END READY DOCUMENT




function split(val) {
    return val.split(/,\s*/);
}

function extractLast(term) {
    return split(term).pop();
}

function update_icon_info_after_load_edit_form(is_update_icon_if_edit_form, formdata_html_text) {
    if (is_update_icon_if_edit_form) {
        formdata = $(formdata_html_text)
        formdata.find('.glyphicon-plus').each(function(index) {
            near_input = $(this).closest('.input-group').find('input[type=text]')
            near_input_value = near_input.val()
            if (near_input_value != '') {
                show_only_glyphicon($(this), 'glyphicon-info-sign')
            }
        })

    }
    return formdata
}

function updateURLParameter(url, param, paramVal) {
    var newAdditionalURL = "";
    var tempArray = url.split("?");
    var baseURL = tempArray[0];
    var additionalURL = tempArray[1];
    var temp = "";
    if (additionalURL) {
        tempArray = additionalURL.split("&");
        for (i = 0; i < tempArray.length; i++) {
            if (tempArray[i].split('=')[0] != param) {
                newAdditionalURL += temp + tempArray[i];
                temp = "&";
            }
        }
    }

    var rows_txt = temp + "" + param + "=" + paramVal;
    return baseURL + "?" + newAdditionalURL + rows_txt;
}

function copyToClipboard(elem) {
    // create hidden text element, if it doesn't already exist
    var targetId = "_hiddenCopyText_";
    var isInput = elem.tagName === "INPUT" || elem.tagName === "TEXTAREA";
    var origSelectionStart, origSelectionEnd;
    if (isInput) {
        // can just use the original source element for the selection and copy
        target = elem;
        origSelectionStart = elem.selectionStart;
        origSelectionEnd = elem.selectionEnd;
    } else {
        // must use a temporary form element for the selection and copy
        target = document.getElementById(targetId);
        if (!target) {
            var target = document.createElement("textarea");
            target.style.position = "absolute";
            target.style.left = "-9999px";
            target.style.top = "0";
            target.id = targetId;
            document.body.appendChild(target);
        }
        target.textContent = elem.textContent;
    }
    // select the content
    var currentFocus = document.activeElement;
    target.focus();
    target.setSelectionRange(0, target.value.length);

    // copy the selection
    var succeed;
    try {
        succeed = document.execCommand("copy");
    } catch (e) {
        succeed = false;
    }
    // restore original focus
    if (currentFocus && typeof currentFocus.focus === "function") {
        currentFocus.focus();
    }

    if (isInput) {
        // restore prior selection
        elem.setSelectionRange(origSelectionStart, origSelectionEnd);
    } else {
        // clear temporary content
        target.textContent = "";
    }
    return succeed;
}
var glyphicon_ARRAYS = ['glyphicon-info-sign', 'glyphicon-plus', 'glyphicon-log-in']

function show_only_glyphicon(dtuong, glyphicon_str) {
    glyphicon_ARRAYS_copy = glyphicon_ARRAYS
    glyphicon_ARRAYS_copy = jQuery.grep(glyphicon_ARRAYS_copy, function(value) {
        return value != glyphicon_str;
    });
    for (i = 0; i < glyphicon_ARRAYS_copy.length; i++) {
        dtuong.removeClass(glyphicon_ARRAYS_copy[i])
    }
    dtuong.addClass(glyphicon_str)
}

function toggleDesAsc(additionalURL) {
    var newAdditionalURL = "";
    tempArray = additionalURL.split("&");
    for (i = 0; i < tempArray.length; i++) {
        key = tempArray[i].split('=')[0]

        if (key != 'sort') {
            newAdditionalURL += "&" + tempArray[i];
        } else {
            paraValue = tempArray[i].split('=')[1]
            if (paraValue.indexOf('-') > -1) {
                console.log('paraValue co - la', paraValue)
                paraValue = paraValue.replace('-', '')
            } else {
                paraValue = '-' + paraValue
            }
            newAdditionalURL += "&" + key + '=' + paraValue;
        }
    }
    return newAdditionalURL
}


function update_parameter_from_table_parameter(table_contain_div, url) {
    desc_th = table_contain_div.find('th.desc:first')
    if (desc_th.length == 0) {
        asc_th = table_contain_div.find('th.asc:first')
        if (asc_th.length == 0) {
            href = table_contain_div.find('.searchtable_header_sort:first').attr('href')
            console.log('khong co asc hoac desc o table')
        } else {
            href = asc_th.find('.searchtable_header_sort').attr('href')
            console.log('co asc class o table', asc_th.length, asc_th.attr('class'))
        }

    } else {
        console.log('co desc class o table', desc_th.length, desc_th.attr('class'), desc_th, desc_th.outerHTML)
        href = desc_th.find('a').attr('href')
    }
    get_question_mark = href.indexOf('?')
    get_parameter = href.substring(get_question_mark + 1)
    get_parameter_toggle = toggleDesAsc(get_parameter)
    if (url.indexOf('?') > -1) {
        url = url + get_parameter_toggle
    } else {
        url = url + '?' + get_parameter_toggle.replace('&', '')
        console.log('@@@@@@@url', url)
    }
    return url

}


var showloading = true
var choosed_command_array_global = []
var model_attr_global
var name_attr_global
var wrapper_attr_global
var BCN_DT_FORMAT = 'HH:mm:SS DD/MM/YYYY'
var DT_FORMAT = 'HH:mm DD/MM/YYYY'
var DATE_FORMAT = 'DD/MM/YYYY'




// D4 fadeIn fadeOut
function d4fadeOutFadeIn(jqueryobject, datahtml) {

    jqueryobject.fadeOut(300);
    jqueryobject.html(datahtml).fadeIn(300);
    jqueryobject.attr('site_id', ui.item.value)
};

function assign_and_fadeoutfadein(jqueryobject, datahtml) {
    if (datahtml) {

        jqueryobject.fadeOut(300);
        jqueryobject.html(datahtml).fadeIn(300);
    }
};

function map_init2(myCenter) {
    var mapProp = {
        center: myCenter,
        zoom: 15,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    var map = new google.maps.Map(document.getElementById("googleMap1"), mapProp);

    var marker = new google.maps.Marker({
        position: myCenter,
    });

    marker.setMap(map);

}

function show_map_from_longlat() {

    long = parseFloat($('#id_Long_3G').val().replace(',', '.'));
    lat = parseFloat($('#id_Lat_3G').val().replace(',', '.'));
    try {
        myCenter = new google.maps.LatLng(lat, long);
        map_init2(myCenter)
    } catch (err) {}
}

function removeParam(key, sourceURL) {
    var rtn = sourceURL.split("?")[0],
        param,
        params_arr = [],
        queryString = (sourceURL.indexOf("?") !== -1) ? sourceURL.split("?")[1] : "";
    if (queryString !== "") {
        params_arr = queryString.split("&");
        for (var i = params_arr.length - 1; i >= 0; i -= 1) {
            param = params_arr[i].split("=")[0];
            if (param === key) {
                params_arr.splice(i, 1);
            }
        }
        rtn = rtn + "?" + params_arr.join("&");
    }
    return rtn;
}


function scrolify_fix_table_header(tblAsJQueryObject, height) {
    var oTbl = tblAsJQueryObject;

    // for very large tables you can remove the four lines below
    // and wrap the table with <div> in the mark-up and assign
    // height and overflow property  
    var oTblDiv = $("<div/>");
    oTbl_height = oTbl.height()
    console.log('oTbl_height', oTbl_height)
    if (oTbl_height < height) {
        return false
    }
    oTblDiv.css({
        'max-height': height,
        'width': oTbl.width()
    });
    //oTblDiv.css('overflow-y','auto').css('overflow-x','initial');
    oTblDiv.attr('class', 'oveflow-y-only')
    oTbl.wrap(oTblDiv);

    // save original width
    oTbl.attr("data-item-original-width", oTbl.width());
    oTbl.find('thead tr th').each(function() {
        $(this).attr("data-item-original-width", $(this).width());
    });
    oTbl.find('tbody tr:eq(0) td').each(function() {
        $(this).attr("data-item-original-width", $(this).width());
    });


    // clone the original table
    var newTbl = oTbl.clone();

    // remove table header from original table
    oTbl.find('thead tr').remove();
    // remove table body from new table
    newTbl.find('tbody tr').remove();

    oTbl.parent().parent().prepend(newTbl);
    newTbl.wrap("<div/>");

    // replace ORIGINAL COLUMN width                
    newTbl.width(newTbl.attr('data-item-original-width'));
    newTbl.find('thead tr th').each(function() {
        $(this).width($(this).attr("data-item-original-width"));
    });
    oTbl.width(oTbl.attr('data-item-original-width'));
    oTbl.find('tbody tr:eq(0) td').each(function() {
        $(this).width($(this).attr("data-item-original-width"));
    });
}

function hasClass(element, cls) {
    return (' ' + element.className + ' ').indexOf(' ' + cls + ' ') > -1;
}
var dtuong_before_submit