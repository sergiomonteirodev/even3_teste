//Carregar preview thumbnail do certificado
var oFReader = new FileReader();
oFReader.readAsDataURL(document.getElementById("uploadImage").files[0]);

oFReader.onload = function (oFREvent) {
document.getElementById("uploadPreview").src = oFREvent.target.result;
};

//Adicionar texto na div conteudo
function addText() {
    var txt = document.getElementById("txt");
    var conteudo = document.getElementById("conteudo");
    conteudo.innerHTML += ''+txt.value+'<br />';
    txt.value = '';
}
//Gerar pdf a partir das tags html

function genPDF(){
        html2canvas(document.getElementById("uploadPreview"), {
            onrendered: function(canvas){
                var img = canvas.toDataURL("image/png");

                var doc = new jsPDF('l', 'mm', 'a4');
                doc.addImage(img, 'JPEG', 10, 10);
                
                doc.fromHTML($('#conteudo').get(0), 50, 50, {'width': 500});

                var xhr = new XMLHttpRequest(); 
                xhr.open('POST', 'http://localhost:5000/certificados/');

                var data = doc.output('arraybuffer');
                xhr.send(data);
                //doc.save('teste2.pdf');
             

            }
        });
}
   
