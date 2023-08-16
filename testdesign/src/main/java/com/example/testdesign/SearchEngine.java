package com.example.testdesign;

import javafx.application.Application;
import javafx.collections.ObservableList;
import javafx.collections.FXCollections;
import javafx.geometry.Insets;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.layout.HBox;
import javafx.scene.layout.VBox;
import javafx.stage.FileChooser;
import javafx.stage.Stage;
import java.io.BufferedReader;
import java.io.*;
import java.io.FileWriter;
import java.nio.file.Files;
import java.util.List;

public class SearchEngine extends Application {

    private TextField searchField;
    private ListView<String> resultList;
    //파일 객체 구현
    private File dbFile;
    private File file;
    //버튼 객체 구현
    private Button searchButton;
    private Button carInputButton;
    private Button carOutputButton;
    private Button selectDbButton;
    private ObservableList<String> searchResult;

    public static void main(String[] args) {                //실제 실행 함수 부분
        launch(args);
    }

    // 검색창에 입력한 데이터를 파일로 저장하는 함수(입고 버튼에 사용되는 함수)
    private void SaveFile(String content, File file) {
        try {
            FileWriter fileWriter = new FileWriter(file, true);
            fileWriter.write(content+ "\n");
            fileWriter.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    @Override
    public void start(Stage stage) {
        stage.setTitle("Search Engine");

        // 검색어 입력 필드
        searchField = new TextField();

        // 검색 버튼
        Button searchButton = new Button("검색");
        searchButton.setOnAction(event -> {
            String searchTerm = searchField.getText();
            // 여기에서 실제 검색 로직을 처리하고 결과를 resultList에 표시하도록 구현
            ObservableList<String> searchResults = search(searchTerm);
            resultList.setItems(searchResults);
        });

        //입고 버튼
        Button carInputButton = new Button("입고");
        carInputButton.setOnAction(event -> {

            FileChooser fileChooser = new FileChooser();
            fileChooser.setTitle("저장할 파일 선택");
            //확장 필터 설정
            fileChooser.getExtensionFilters().add(new FileChooser.ExtensionFilter("Text Files", "*.txt"));
            File selectedFile = fileChooser.showOpenDialog(stage);
            //저장하는 메서드
            if(selectedFile != null){
                SaveFile(searchField.getText(), selectedFile);
                resultList.setItems(FXCollections.observableArrayList("해당 정보가 저장되었습니다."));
            }
            if (searchField.getText() != null) {
                System.out.println("입고 할 데이터를 입력해주십시오.");
            }
        });

            /*
            출고 버튼 구현

            0. 출고 버튼 객체 생성. -해결
            0-1. textfield에 정보를 검색하고
            0-2. 나온 검색결과를 선택하고
                 출고 버튼을 누른다.
            0-3. 선택한 결과에 exist 문자열이 있는지 확인하고
            0-4. 있다면, exist 문자열을 out로 치환한다.
            0-5. 없다면, "already out" 출력.

            검색결과에서 선택한것에 exist가 있는지 판단부터.
            3. selected == true 면 selected에 'exist'가 있는지 판별
            3-1. exitst가 있는지 판별하는 메서드 필요
            4. contains() 사용?
             */

        Button carOutputButton = new Button("출고");
        carOutputButton.setOnAction(event -> {
            // 선택한 차량의 정보를 출력
            String selectedCarInfo = resultList.getSelectionModel().getSelectedItem();

            if (selectedCarInfo != null) {
                // 선택한 차량의 정보를 txt 파일에서 변경
                FileChooser fileChooser2 = new FileChooser();
                fileChooser2.setTitle("파일 선택");
                fileChooser2.getExtensionFilters().add(new FileChooser.ExtensionFilter("Text Files", "*.txt"));
                File selectedFile2 = fileChooser2.showOpenDialog(stage);

                if (selectedFile2 != null) {
                    try {
                        List<String> lines = Files.readAllLines(selectedFile2.toPath());
                        for (int i = 0; i < lines.size(); i++) {
                            if (lines.get(i).equals(selectedCarInfo) && lines.get(i).contains("exist")) {
                                lines.set(i, lines.get(i).replace("exist", "sold"));
                                try (FileWriter fileWriter = new FileWriter(selectedFile2)) {
                                    for (String line : lines) {
                                        fileWriter.write(line + "\n");
                                    }
                                    System.out.println("수정 완료");
                                } catch (IOException e) {
                                    e.printStackTrace();
                                }
                                return;
                            }
                        }
                        System.out.println("exist가 포함된 내용이 아닙니다.");
                    } catch (IOException e) {
                        e.printStackTrace();
                    }
                } else {
                    System.out.println("파일을 선택해주세요.");
                }
            } else {
                System.out.println("선택한 내용이 없습니다.");
            }
        });

        //==================================================================//

        // 결과 목록
        resultList = new ListView<>();

        // DB 파일 선택 버튼
        Button selectDbButton = new Button("DB 파일 선택");
        selectDbButton.setOnAction(event -> {
            FileChooser fileChooser = new FileChooser();
            fileChooser.setTitle("DB 파일 선택");
            // DB 파일 필터링 (확장자가 .txt인 파일)
            fileChooser.getExtensionFilters().add(new FileChooser.ExtensionFilter("Text Files", "*.txt"));
            File selectedFile = fileChooser.showOpenDialog(stage);  //showOpenDialog 를 사용하면 파일 또는 폴더를 열 수 있음.
            //저장 대화 상자는 사용자에게 대화 상자를 표시하고 선택한 경로가 포함 된 경로를 반환합니다.
            if (selectedFile != null) {
                dbFile = selectedFile;
                // DB 파일 선택 후 초기화 메시지 표시
                resultList.setItems(FXCollections.observableArrayList("DB 파일이 선택되었습니다."));
            }
        });

        // 검색 버튼 레이아웃 (수평 레이아웃)
        HBox BtnLayout = new HBox(10);
        BtnLayout.setPadding(new Insets(10));
        BtnLayout.getChildren().addAll(searchButton, carInputButton, carOutputButton);

        VBox totalLayout = new VBox(10);
        totalLayout.setPadding(new Insets(10));
        totalLayout.getChildren().addAll(searchField, BtnLayout, resultList, selectDbButton);

        // 씬 생성
        Scene scene = new Scene(totalLayout, 300, 200);
        stage.setScene(scene);
        stage.show();
    }

    // DB 파일에서 검색어를 찾아서 결과를 반환하는 메서드

    private ObservableList<String> search(String searchTerm) {
        ObservableList<String> searchResults = FXCollections.observableArrayList();
        if (dbFile == null) {
            searchResults.add("DB 파일을 선택해주세요.");
            return searchResults;
        }

        try (BufferedReader reader = new BufferedReader(new FileReader(dbFile))) {
            String line;
            while ((line = reader.readLine()) != null) {
                if (line.contains(searchTerm)) {
                    searchResults.add(line);
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        if (searchResults.isEmpty()) {
            searchResults.add("검색 결과가 없습니다.");
        }
        return searchResults;
    }
}