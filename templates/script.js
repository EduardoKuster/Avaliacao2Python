$(function () {
    $(document).on("click", "#btnInserirPessoa", function () {
        nome = $("#nomepessoa").val();
        cpf = $("#cpfpessoa").val();
        email = $("#emailpessoa").val();
        var dados = JSON.stringify({
            nome: nome,
            cpf: cpf,
            email: email
        });
        $.ajax({
            url: 'http://localhost:5000/incluirPessoas',
            type: 'POST',
            dataType: 'json',
            contentType: 'application/json',
            data: dados,
            success: alert('pessoa criada com sucesso'),
            error: function () {
                alert("Falha ao salvar nova pessoa");
            }
        });
    });

    $(document).on("click", "#btnInserirDisciplina", function () {
        nome = $("#nomedisciplina").val();
        cargaHoraria = $("#cargadisciplina").val();
        ementa = $("#ementadisciplina").val();
        var dados = JSON.stringify({
            nome: nome,
            cargaHoraria: cargaHoraria,
            ementa: ementa
        });
        $.ajax({
            url: 'http://localhost:5000/incluirDisciplinas',
            type: 'POST',
            dataType: 'json',
            contentType: 'application/json',
            data: dados,
            success: alert('Disciplina criada com sucesso'),
            error: function () {
                alert("Falha ao salvar nova disciplina");
            }
        });
    });

    $.ajax({
        url: 'http://localhost:5000/listarPessoasJson',
        method: 'GET',
        dataType: 'json',
        success: function opcoesPessoas(Pessoas) {            
            for (var p in Pessoas) {
                //preencher select com as pessoas cadastradas
                $('#selectPessoa').append(`<option value='${Pessoas[p].id}'>${Pessoas[p].nome}</option>`);
            }
        },
        error: function () {
            alert("Falha ao buscar lista de pessoas");
        }
    });
    
    $.ajax({
        url: 'http://localhost:5000/listarDisciplinasJson',
        method: 'GET',
        dataType: 'json',
        success: function opcoesPessoas(Disciplinas) {            
            for (var p in Disciplinas) {
                //preencher select com as Disciplinas cadastradas
                $('#selectDisciplina').append(`<option value='${Disciplinas[p].id}'>${Disciplinas[p].nome}</option>`);
            }
        },
        error: function () {
            alert("Falha ao buscar lista de Disciplinas");
        }
    });

    $(document).on("click", "#btnInserirEstudanteDisciplina", function () {
        semestre = $("#semestreestudante").val();
        mediaFinal = $("#mediaestudante").val();
        frequencia = $("#frequenciaestudante").val();
        pessoaId = $("#selectPessoa").find(":selected").val();
        disciplinaId = $("#selectDisciplina").find(":selected").val();
        alert(pessoaId)
        var dados = JSON.stringify({
            semestre: semestre,
            mediaFinal: mediaFinal,
            frequencia: frequencia,
            pessoaId: pessoaId,
            disciplinaId: disciplinaId
        });

        $.ajax({
            url: 'http://localhost:5000/incluirEstudanteDisciplina',
            type: 'POST',
            dataType: 'json',
            contentType: 'application/json',
            data: dados,
            success: alert('Estudante da Disciplina criada com sucesso'),
            error: function () {
                alert("Falha ao salvar novo estudante de disciplina");
            }
        });
    });

});