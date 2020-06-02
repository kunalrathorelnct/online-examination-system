$(document).ready(function() {
    const constraints = {
        video: true
      };
      
    const video = document.querySelector('video');
      
    navigator.mediaDevices.getUserMedia(constraints).then((stream) => {video.srcObject = stream});



    var countDownDate = new Date("Jun 2, 2020 15:37:25").getTime();
    var x = setInterval(function() {
    var now = new Date().getTime();
    var distance = countDownDate - now;
    var days = Math.floor(distance / (1000 * 60 * 60 * 24));
    var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    var seconds = Math.floor((distance % (1000 * 60)) / 1000);
    $("#timer").html(days + "d " + hours + "h " + minutes + "m " + seconds + "s ");
    if (distance < 0) {
        clearInterval(x);
        $("#timer").html("EXPIRED");
      }
    }, 1000);


    $("#calculator").click(function(){
        $("#overlay").removeClass("d-none");
        $("#overlayframe1").html("<iframe src=https://widgetscode.com/wc/sciv/all?skin=nb1 style='width:560px;height:670px;margin:0;'frameborder=0></iframe>");
        

    });
    
    $("#close").click(function(){
        $("#overlay").addClass("d-none");
    });

    var i=1;
    $("#panel"+i).removeClass("not_visited");
    $("#panel"+i).addClass("not_answered");
    $("#iframeid").contents().find("#id"+i).removeClass("d-none");
    $("#reviewNext").click(function(){
        console.log(i);
        $("#panel"+i).removeClass();
        if($("#iframeid").contents().find("input[name=exampleRadios"+i+"]").is(":checked")){
            
            $("#panel"+i).addClass("normal answer_marked");
        }else{
            $("#panel"+i).addClass("normal marked");
        }
        $("#iframeid").contents().find("#id"+i).addClass("d-none");
        
        i+=1;
        if(i==maxx){
            $("#reviewNext").addClass("disabled");
            $("#saveNext").html("Save");
        }
        $("#iframeid").contents().find("#id"+i).removeClass("d-none");
        if($("#panel"+i).hasClass("not_visited")){
            $("#panel"+i).removeClass("not_visited");
            $("#panel"+i).addClass("not_answered");
        }
        
    });
    $("#clearResponse").click(function(){
        $("#panel"+i).removeClass();
        $("#panel"+i).addClass("normal not_answered");
        $("#iframeid").contents().find("input[name=exampleRadios"+i+"]").prop("checked", false);
    });
    $panelClick =function($this) {
        $("#iframeid").contents().find("#id"+i).addClass("d-none");
        i = parseInt($this.attr('id').replace('panel', ''));
        $("#iframeid").contents().find("#id"+i).removeClass("d-none");
        if($("#panel"+i).hasClass("not_visited")){
            $("#panel"+i).removeClass("not_visited");
            $("#panel"+i).addClass("not_answered");
        }
        if(i==maxx){
            $("#reviewNext").addClass("disabled");
            $("#saveNext").html("Save");
        }else{
            $("#reviewNext").removeClass("disabled");
            $("#saveNext").removeClass("disabled");
        }

    };
    $("#submitBtn").click(function(){
        
    });
    $("#saveNext").click(function(){
        $("#panel"+i).removeClass();
        if($("#iframeid").contents().find("input[name=exampleRadios"+i+"]").is(":checked")){
            $("#panel"+i).addClass("normal answered");
        }
        else{
            $("#panel"+i).addClass("normal not_answered");
        }
        
        if(i!=maxx){
            $("#iframeid").contents().find("#id"+i).addClass("d-none");
            i+=1;
            if(i==maxx){
                $("#reviewNext").addClass("disabled");
                $("#saveNext").html("Save");
        
            }
            $("#iframeid").contents().find("#id"+i).removeClass("d-none");
            if($("#panel"+i).hasClass("not_visited")){
                $("#panel"+i).removeClass("not_visited");
                $("#panel"+i).addClass("not_answered");
            }
         }

    });
});