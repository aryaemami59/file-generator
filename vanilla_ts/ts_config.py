from create_file import TS_CONFIG_JSON


ts_config = TS_CONFIG_JSON(
    {
        "compilerOptions": {
            "esModuleInterop": True,
            "forceConsistentCasingInFileNames": True,
            "isolatedModules": True,
            "module": "ESNext",
            "moduleResolution": "Node",
            "noEmit": True,
            "noImplicitAny": True,
            "useUnknownInCatchVariables": True,
            "strictFunctionTypes": True,
            "noUncheckedIndexedAccess": True,
            "useDefineForClassFields": True,
            "resolveJsonModule": True,
            "skipLibCheck": True,
            "strict": True,
            "strictNullChecks": True,
            "target": "ESNext",
        },
    },
)
