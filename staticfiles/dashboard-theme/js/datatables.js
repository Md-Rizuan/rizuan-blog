$(function (e) {

    // basic datatable
    $('#datatable-basic').DataTable({
        language: {
            searchPlaceholder: 'Search...',
            sSearch: '',
        },
        "pageLength": 10,
        // scrollX: true
    });
    // basic datatable

    // responsive datatable
    // $('#responsiveDataTable').DataTable({
    //     responsive: true,
    //     paging: false,
    //     searching: false,
    //     responsive: true, 
    //     bDestroy: true,
    //     info: false,
    //     ordering: false,
    //     autoWidth: false,
    //     "order": [],
    //     columnDefs: [
    //         { responsivePriority: 1, targets: 0 },
    //         { responsivePriority: 2, targets: -1 },
    //     ],
    // });

    if (!$.fn.DataTable.isDataTable('#responsiveDataTable')) { 
        $("#responsiveDataTable").DataTable({
            responsive: true,
            paging: false,
            searching: false,
            responsive: true, 
            bDestroy: true,
            info: false,
            ordering: false,
            autoWidth: false,
            "order": [],
            columnDefs: [
                { responsivePriority: 1, targets: 0 },
                { responsivePriority: 2, targets: -1 },
            ],
        });
    }

//     if (window.innerWidth <= 991) { 
        
//         if (!$.fn.DataTable.isDataTable('#responsiveDataTable')) { 
//             $("#responsiveDataTable").DataTable({
//                 responsive: true,
//                 paging: false,
//                 searching: false,
//                 responsive: true, 
//                 bDestroy: true,
//                 info: false,
//                 ordering: false,
//                 autoWidth: false,
//                 "order": [],
//                 columnDefs: [
//                     { responsivePriority: 1, targets: 0 },
//                     { responsivePriority: 2, targets: -1 },
//                 ],
//             });
//         }
//     } else {
        
//         if ($.fn.DataTable.isDataTable('#responsiveDataTable')) {
//             $('#responsiveDataTable').DataTable().destroy();
//         }
//     }
    // responsive datatable

    // responsive modal datatable
    $('#responsivemodal-DataTable').DataTable({
        responsive: {
            details: {
                display: $.fn.dataTable.Responsive.display.modal({
                    header: function (row) {
                        var data = row.data();
                        return data[0] + ' ' + data[1];
                    }
                }),
                renderer: $.fn.dataTable.Responsive.renderer.tableAll({
                    tableClass: 'table'
                })
            }
        },
        language: {
            searchPlaceholder: 'Search...',
            sSearch: '',
        },
        "pageLength": 10,
    });
    // responsive modal datatable

    // file export datatable
    $('#file-export').DataTable({
        dom: 'Bfrtip',
        buttons: [
            'copy', 'csv', 'excel', 'pdf', 'print'
        ],
        language: {
            searchPlaceholder: 'Search...',
            sSearch: '',
        },
    });
    // file export datatable

    // delete row datatable
    var table = $('#delete-datatable').DataTable({
        language: {
            searchPlaceholder: 'Search...',
            sSearch: '',
        }
    });
    $('#delete-datatable tbody').on('click', 'tr', function () {
        if ($(this).hasClass('selected')) {
            $(this).removeClass('selected');
        }
        else {
            table.$('tr.selected').removeClass('selected');
            $(this).addClass('selected');
        }
    });
    $('#button').on("click", function () {
        table.row('.selected').remove().draw(false);
    });
    // delete row datatable

    // scroll vertical
    $('#scroll-vertical').DataTable({
        scrollY: '265px',
        scrollCollapse: true,
        paging: false,
        scrollX: true,
        language: {
            searchPlaceholder: 'Search...',
            sSearch: '',
        },
    });
    // scroll vertical

    // hidden columns
    $('#hidden-columns').DataTable({
        columnDefs: [
            {
                target: 2,
                visible: false,
                searchable: false,
            },
            {
                target: 3,
                visible: false,
            },
        ],
        language: {
            searchPlaceholder: 'Search...',
            sSearch: '',
        },
        "pageLength": 10,
        // scrollX: true
    });
    // hidden columns
    
    // add row datatable
    var t = $('#add-row').DataTable({
        
        language: {
            searchPlaceholder: 'Search...',
            sSearch: '',
        },
    });
    var counter = 1;
    $('#addRow').on('click', function () {
        t.row.add([counter + '.1', counter + '.2', counter + '.3', counter + '.4', counter + '.5']).draw(false);
        counter++;
    });
    // add row datatable

});

