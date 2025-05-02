mkdir -p ai_snapshot
rsync -av --exclude='__pycache__/' --exclude='venv*/' --exclude='.git/' --exclude="ai_snapshot/" --exclude='.gitignore' ./ ai_snapshot/

if ! command -v 7z
then
    echo "No se encontró 7z. Favor de instalar."
    exit 1
fi

 7z a ai_snapshot.$(date +%Y.%m.%d_%H.%M.%S).7z -mhe -p ./ai_snapshot/

 rm -r ai_snapshot/

