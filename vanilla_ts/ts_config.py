from create_file import TS_CONFIG_JSON


ts_config = TS_CONFIG_JSON(
    {
        "compilerOptions": {
            "target": "ES2022",
            "module": "ES2022",
            "moduleResolution": "node",
            "resolveJsonModule": True,
            "esModuleInterop": True,
            "forceConsistentCasingInFileNames": True,
            "strict": True,
            "noUnusedLocals": True,
            "noUnusedParameters": True,
            "skipLibCheck": True,
        }
    },
)
# ts_config = File_In_Current_Dir(
#     "tsconfig",
#     "json",
#     """{
#   "compilerOptions": {
#     "target": "ES2022",
#     "module": "ES2022",
#     "moduleResolution": "node",
#     "resolveJsonModule": True,
#     "esModuleInterop": True,
#     "forceConsistentCasingInFileNames": True,
#     "strict": True,
#     "noUnusedLocals": True,
#     "noUnusedParameters": True,
#     "skipLibCheck": True
#   }
# }
# """,
# )
