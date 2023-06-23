from create_file import TS_CONFIG_JSON


ts_config = TS_CONFIG_JSON(
    {
        "compilerOptions": {
            "target": "ESNext",
            "module": "ESNext",
            "moduleResolution": "Node",
            "esModuleInterop": True,
            "forceConsistentCasingInFileNames": True,
            "strict": True,
            "noEmit": True,
            "noImplicitAny": True,
            "isolatedModules": True,
            "resolveJsonModule": True,
            "skipLibCheck": True,
        },
    },
)
