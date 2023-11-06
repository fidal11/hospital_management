$(document).ready(function() {
    // Event listener for the department dropdown
    $('#department-select').on('change', function() {
        var departmentId = $(this).val();
        
        // Clear existing doctor, date, time, and slot options
        $('#doctor-select, #date-select, #time-select, #slot-select').empty();
        
        // Send an AJAX request to get doctors for the selected department
        $.ajax({
            url: '/get_doctors/',
            data: { department_id: departmentId },
            dataType: 'json',
            success: function(data) {
                var doctorSelect = $('#doctor-select');
                doctorSelect.append($('<option>').text('Select Doctor').attr('value', ''));
                $.each(data, function(index, doctor) {
                    doctorSelect.append($('<option>').text(doctor.name).attr('value', doctor.id));
                });
            }
        });
    });
    
    // Event listener for the doctor dropdown
    $('#doctor-select').on('change', function() {
        var doctorId = $(this).val();
        
        // Clear existing date, time, and slot options
        $('#date-select, #time-select, #slot-select').empty();
        
        // Send an AJAX request to get available dates for the selected doctor
        $.ajax({
            url: '/get_dates/',
            data: { doctor_id: doctorId },
            dataType: 'json',
            success: function(data) {
                var dateSelect = $('#date-select');
                dateSelect.append($('<option>').text('Select Date').attr('value', ''));
                $.each(data, function(index, date) {
                    dateSelect.append($('<option>').text(date).attr('value', date));
                });
            }
        });
    });
    
    // Event listener for the date dropdown
    $('#date-select').on('change', function() {
        var selectedDate = $(this).val();
        
        // Clear existing time and slot options
        $('#time-select, #slot-select').empty();
        
        // Send an AJAX request to get available times for the selected date and doctor
        var doctorId = $('#doctor-select').val();
        $.ajax({
            url: '/get_times/',
            data: { doctor_id: doctorId, date: selectedDate },
            dataType: 'json',
            success: function(data) {
                var timeSelect = $('#time-select');
                timeSelect.append($('<option>').text('Select Time').attr('value', ''));
                $.each(data, function(index, time) {
                    timeSelect.append($('<option>').text(time).attr('value', time));
                });
            }
        });
    });

    // Event listener for the time dropdown
    $('#time-select').on('change', function() {
        var selectedDate = $('#date-select').val();
        var selectedTime = $(this).val();
        
        // Clear existing slot options
        $('#slot-select').empty();
        
        // Send an AJAX request to get available slots for the selected date, time, and doctor
        var doctorId = $('#doctor-select').val();
        $.ajax({
            url: '/get_slots/',
            data: { doctor_id: doctorId, date: selectedDate, time: selectedTime },
            dataType: 'json',
            success: function(data) {
                var slotSelect = $('#slot-select');
                slotSelect.append($('<option>').text('Select Slot').attr('value', ''));
                $.each(data, function(index, slot) {
                    slotSelect.append($('<option>').text(slot.time).attr('value', slot.id));
                });
            }
        });
    });
});





// my work

$('#doctor-select').change(function(){
    var doctorId = $(this).val();
    $.ajax({
        url:'/get_slot/',
        data:{doctor_id:doctorId},
        dataType:'json',
        success: function(data){
            console.log(doctorId)
            var daySelect = $('#day-select');
            daySelect.empty();
            $.each(data, function(index, slot){
                daySelect.append($('<option>').text(slot.day).attr('value', slot.id));
            });
        }
    });
});