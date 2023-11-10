# **Note Backup Tool**

This tool is a command-line interface (CLI) application designed for managing and backing up notes. It provides functionalities to list, retrieve, and display information about notes and the user.

## **Installation**

To install this package directly from the main branch on GitHub, use the following pip command:

```
pip install git+https://github.com/qtysdk/note-backup-tool.git@main
```

## **Usage**

The application provides the following commands:

### **List Notes**

- Command: **`nbc list`**
- Description: Lists all the notes. It has an option to display the notes in a table format.

```bash
$ nbc list
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ ID                     ┃ Title                                                      ┃               Published At ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ EfjgPeIrS3WGo2qy4MqQKw │ Reading and modifying the source code of the dbt adapter   │              not published │
│ cK6MxaFmSmWYSMAaGEHK1w │ 出包魔法師 6b62e9cb                                        │ 2023-07-08T19:31:46.104000 │
│ P06CKqRzQCiVuoYHCx9uOA │ Python 開發環境準備                                        │ 2023-07-02T13:08:01.916000 │
│ TuBAeGfYQS2kyw-5wkS-lg │ 學習者的輸入與輸出測試                                     │ 2023-06-28T08:56:23.679000 │
│ tBFDmK4eS2-OR3ctXfBYhA │ 遊戲微服務的 GitHub Actions 入門                           │ 2023-06-20T13:09:20.131000 │
│ HnIP0AzFR_eaWDODroVn5w │ OOA 結構化分析怎麼做 (極簡版)                              │ 2023-06-09T23:51:29.305000 │
│ emB3Tml1QYCihoW6l3kg9w │ Recap [三國殺] 練習 ATDD/TDD 基本流程                      │ 2023-06-06T12:19:07.095000 │
│ komcC-rEQQS2FCZftmyPJw │ 由 Walking Skeleton 到 Iteration 0                         │ 2023-06-03T13:27:39.935000 │
│ T9ls4NpgRhi2y777lGSymQ │ 女巫的佳釀初回 ATDD 內容回顧                               │ 2023-05-28T11:57:21.403000 │
│ 94vjcuvrRhiicqnD-5qAag │ Practice Stack 導覽                                        │ 2023-04-14T20:46:29.573000 │
│ DV8M7JOHQHa9cbaHpFOPWw │ 來場輕便可攜的 Event Storming 吧！                         │ 2023-04-16T23:40:25.784000 │
│ ssA8CcU-Q1ikiQ0n00rriQ │ 2023 Q1 產出盤點                                           │ 2023-03-29T13:40:17.764000 │
│ nwcD00WFRu6wsayW5NtXYg │ TWJUG-LITE 26 TDD Workshop                                 │ 2023-03-08T19:44:13.863000 │
│ A9xC9H8sSVahX6Z8VYLaUw │ 跟 ChatGPT 一起 Pair Programming                           │ 2023-02-28T11:28:00.496000 │
│ ps5wn8ozS1mUrecUEdistg │ 也來讀讀 Open Source 函式庫怎麼實作 Discord Gateway 的部分 │ 2023-02-19T20:31:35.096000 │
│ R0ACyxSKTiCDGqnKYKdFhA │ Discord 基礎範例調查兵團 [3]                               │ 2023-02-07T00:15:27.557000 │
│ VRlXF7dwTxS3ZGkGwZySKg │ Discord 基礎範例調查兵團 [2]                               │ 2023-02-06T18:26:43.247000 │
│ 0aCkfiP4TQ6kfSO46CO3LA │ Discord 基礎範例調查兵團 [1]                               │ 2023-02-05T20:12:04.081000 │
│ VpTYR6XDQgSY9FR0NJ1NCw │ 跟著 Discord 官方教學啟動範例程式                          │ 2023-02-03T17:42:39.101000 │
│ xp3Npo4JQQ2TNHetsryvOg │ 使用 chroot 簡單隔離                                       │ 2023-02-01T21:41:40.422000 │
│ B9eKCJuFSUGXmbD18CpY0A │ Database 的 Index 是什麼？                                 │ 2023-01-27T17:08:44.343000 │
│ J5AtE9F8SeqRe4_DoarYiw │ Conda 與多版本 Python                                      │ 2023-01-03T10:33:45.882000 │
│ 6wt5C8J7RFW9uBZ3-XNrFg │ DrogonTest 準備好上戰場了嗎？                              │ 2022-12-25T01:23:08.840000 │
│ ny7DeZZ0RyySjygMgMIRjQ │ 骰子街 C++ 編譯問題                                        │ 2022-12-21T08:30:36.419000 │
│ BhwEIPHhTUO5Aw5Sz8uE0Q │ 學習程式語言也順便學習 Python (cs61a)                      │ 2022-12-17T17:05:55.709000 │
│ NiuUtYA9Qge_GpeWwMQ4wg │ [筆記] 物件導向分析                                        │ 2023-04-13T16:16:17.417000 │
│ Qyc-ZeUZQPu9nPHA7fRviQ │ [電影欣賞] DevOps 潮流下的 API First 開發策略              │ 2022-12-04T17:38:34.030000 │
│ 5Zyp86a9RJafQ8ZA1zkzzg │ 走了啊～ 來 TDD 辣！                                       │              not published │
│ HkSWXVj3SSKJsLEZ3KciyQ │ 也來玩玩 skaffold 好了                                     │ 2019-11-30T22:32:11.354000 │
│ Yuz5c4YRTRyAdKy_zpoC2Q │ skaffold labs                                              │              not published │
└────────────────────────┴────────────────────────────────────────────────────────────┴────────────────────────────┘
```

### **Get Note**

- Command: **`nbc get [NOTE_ID]`**
- Description: Fetches and converts a specific note identified by its ID. The converted note is then saved as a markdown file named **`[NOTE_ID].md`**

Additionally, if the note contains any image URLs, these images will be downloaded and saved in the **`images/`** directory. The image links in the markdown file will be updated to point to these local copies in the **`images/`** directory.

```bash
$ nbc get VpTYR6XDQgSY9FR0NJ1NCw
Note saved as VpTYR6XDQgSY9FR0NJ1NCw.md
```

### **User Information**

- Command: **`nbc me`**
- Description: Displays details of the current user's profile, such as username, email, and other relevant settings or status information.


```bash
$ nbc me
                                 User Information
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ ID                                   ┃ Name          ┃ Email                    ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ 883e3494-19be-400a-a087-ad8354765566 │ Ching-Yi Chan │ chingyichan.tw@gmail.com │
└──────────────────────────────────────┴───────────────┴──────────────────────────┘
```

## **Configuration**

In order to use the Note Backup Tool, some configuration steps are required:

- **Setting up the NBC_HACKMD_API_TOKEN Environment Variable**: This application requires an API token to interact with the HackMD API. You will need to set the **`NBC_HACKMD_API_TOKEN`** environment variable with your HackMD API token. This can be done as follows:
    
    On Linux or macOS:
    
    ```bash
    export NBC_HACKMD_API_TOKEN='your_api_token_here'
    ```
    
    On Windows Command Line:
    
    ```
    set NBC_HACKMD_API_TOKEN=your_api_token_here
    ```
    
    On Windows PowerShell:
    
    ```powershell
    $env:NBC_HACKMD_API_TOKEN='your_api_token_here'
    ```
    
    Replace **`your_api_token_here`** with your actual API token.